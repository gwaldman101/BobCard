from django.shortcuts import render
from .models import Student, StudentEntry, Location
from django.views import generic
from django import forms
from django.utils import timezone
from django.shortcuts import get_object_or_404
import datetime
from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions
# Create your views here.
from .forms import RequestAccessForm
def index(request):

    """View function for home page of site."""
    print("I am here")
    name = "Ann"
    return render(request,
     'index.html', 
     context={
         'name': name
     })
#### ON POST:
### IF IN REDIS LIST: 
    #### REDIRECT TO ACCEPT PAGE
## IF NOT IN REDIS redicrect to deny page
# Posgress permanent
# when fetch value 
# - take value from redis, 
# - not searching in posgres
# - use REdis short term storage:
# - if redis does not return then 

# trigger on when datetime.now() = requested + entry_time
# pub/sub 


def authorize(request, location,net_id, time ):
    # save in posgres
    print("nn authorize")
    #location_to_id = [{}]

    #if not in cache and not in db then no access
    
    already_authorized = StudentEntry.objects.filter(net_id=net_id).exists()
    if(already_authorized):
        # entry exists:
        return render(request,'accept.html',context={'net_id': net_id})
    else:
        # add them to database:



        print("?")

    #return render(request,'authorize.html',context={'net_id': net_id,'location': location,'time_requested': time_requested})
        return render(request,'authorize.html',context={'net_id': net_id})


def request_access(request):
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )
    
    name = request.POST.get("id")
    location = request.POST.get("location")
    time = request.POST.get("time")
    location = Location.objects.get(name = location)
    if (Student.objects.filter(net_id = name).exists()):
        student = Student.objects.get(net_id = name)
    else:
        student = Student.objects.create(net_id = name)

        
    start =timezone.localtime(timezone.now())
    seconds = int(time) * 60
    end = start + datetime.timedelta(0,seconds) # days, seconds, then other fields.
    print(start.time())
    print(end.time())
    student = Student.objects.get(net_id = name)
    student_entry = StudentEntry(
            net_id = student,
            entry_time = start,
            end_time = end,
            requested_location = location
        )
    student_entry.save()
    delete_entry(student_entry.net_id.net_id,schedule=end )
   
    name = "http://35.237.10.156:8000/home/?fbclid=IwAR1w5bKz9S0SDj3zTFiPtjNMpwrPAop7CIkxfRbf6i-PQ6g7A8vTOwP8tRU"
    return render(request,
     'request_access.html',context={
         'name': name, 
         'valid':end.time()
     })

def myview(request):
    # Build context for rendering QR codes.
    return render(request, 'home/index.html', {'form': form, 'student_entry':student_entry}, context=context)
    

# background job
from background_task import background
from .models import StudentEntry

@background(schedule=5)
def delete_entry(entry_id):

    StudentEntry.objects.filter(net_id = entry_id).delete()
