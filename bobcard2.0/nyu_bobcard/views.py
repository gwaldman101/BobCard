#from django.shortcuts import render
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework import status
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# everything above this line is imports that I added for the tutorial: https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178

from django.shortcuts import render
from .models import Student, StudentEntry, Location
from django.views import generic
from django import forms
from django.shortcuts import get_object_or_404
import datetime
from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions
# Create your views here.
def index(request):


    """View function for home page of site."""
    print("I am here")
    name = "Ann"
    return render(request,
     'index.html', 
     context={
         'name': name
     })

@cache_page(CACHE_TTL)
def authorize(request, location,net_id ):

    print("authorizing")

    comp_key = net_id + location

    if comp_key in cache:
        print('Found in cache')
        return render(request, 'success.html')
    else:
        already_authorized = StudentEntry.objects.filter(net_id=netid, requested_location_id = location_id).exists()

  
        if(already_authorized):
            print('Found in database but not in cache')
            cache.set(comp_key, entry, timeout=CACHE_TTL)
            return render(request, 'success.html')
        else:
            print('Not found anywhere')
            return render(request, 'fail.html')




def authorizeWithoutCache(request, location,net_id, time ):
    # save in posgres
    print("nn authorize")
    #location_to_id = [{}]
    already_authorized = StudentEntry.objects.filter(net_id=netid, requested_location_id = location_id).exists()
    if(already_authorized):
        # entry exists:
        return render(request, 'success.html')
    else:
        return render(request, 'fail.html')






@cache_page(CACHE_TTL)
def request_access(request):
    """View function for renewing a specific StudentEntry by librarian."""
    print("we made it,yayy")
    print('Student', StudentEntry.objects.count())
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )
    
    name = request.POST.get("id")
    location = request.POST.get("location")
    time = request.POST.get("time")
    if location is None or name is None: 
        return redirect('/home')
    name = name.strip(",()")
    location = location.strip(",()")
    location = Location.objects.get(name=location)
    if (Student.objects.filter(net_id = name).exists()):
        student = Student.objects.get(net_id = name)
    else:
        student = Student.objects.create(net_id = name)

    start =timezone.localtime(timezone.now())
    seconds = int(time) * 60
    end = start + datetime.timedelta(0,seconds) # days, seconds, then other fields.ts.get(net_id = name)
    student_entry = StudentEntry(
            net_id = student,
            entry_time = start,
            end_time = end,
            requested_location = location
        )
    # add to db
    student_entry.save()
    delete_entry(student_entry.net_id.net_id,schedule=end )
    loc_id =location.location_id
    
    comp_key = name + request.POST.get("location")
    comp_value = name + " is authorized"
    cache.set(comp_key, comp_value, timeout=CACHE_TTL)
    print('added key:value to cache')

    name = "http://127.0.0.1:8000/home/authorize/" + str(loc_id) +  "/" + str(name)
    print(name)
    return render(request,
     'request_access.html',context={
         'name': name, 
         'valid':end.time()
     })

    # # If this is a GET (or any other method) create the default form
    
    # context = {
    #     'form': form,
    #     'student_entry': student_entry,
    # }
def scanned_qr(request, location_id, netid):
    print("IN SCANNED")
    print(location_id)
    print(netid)

    #if the user is in the system for that location
    exists = StudentEntry.objects.filter(net_id=netid, requested_location_id = location_id).exists()

    if exists:
        return render(request, 'success.html')
    else:
        return render(request, 'fail.html')



def myview(request):
    # Build context for rendering QR codes.
    


    

    return render(request, 'home/index.html', {'form': form, 'student_entry':student_entry}, context=context)
    

# background job
from background_task import background
from .models import StudentEntry

@background(schedule=5)
def delete_entry(entry_id):

    StudentEntry.objects.filter(net_id = entry_id).delete()