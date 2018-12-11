from django.shortcuts import render
from .models import Student, StudentEntry, Location
from django.views import generic
from django import forms
from django.utils import timezone
from django.shortcuts import get_object_or_404
import datetime
from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions
from django.shortcuts import redirect
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

def request_access(request):
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

    name = request.POST.get("id")
    location = request.POST.get("location")
   

    time = request.POST.get("time")
    location_exists = Location.objects.filter(name=location).exists()
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
    end = start + datetime.timedelta(0,seconds) # days, seconds, then other fields.
    student_entry = StudentEntry(
            net_id = student,
            entry_time = start,
            end_time = end,
            requested_location = location
    )
    student_entry.save()
    delete_entry(student_entry.net_id.net_id,schedule=end )
    
    loc_id =location.location_id
    

    #name = "http://35.237.10.156:8000/home/?fbclid=IwAR1w5bKz9S0SDj3zTFiPtjNMpwrPAop7CIkxfRbf6i-PQ6g7A8vTOwP8tRU"
    name = "http://127.0.0.1:8000/home/authorize/" + str(loc_id) +  "/" + str(name)
    print(name)
    return render(request,
     'request_access.html',context={
         'name': name, 
         'valid':end.time()
     })

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