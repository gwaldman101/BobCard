from django.shortcuts import render
from .models import Student, StudentEntry, Location
from django.views import generic
from django import forms
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
    """View function for renewing a specific StudentEntry by librarian."""
    print("we made it,yayy")
    print('Student', StudentEntry.objects.count())
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
        student.location.set([location])

        
    start = datetime.datetime.now()
#    a = datetime.datetime(100,1,1,11,34,59)
    seconds = int(time) * 60
    end = start + datetime.timedelta(0,seconds) # days, seconds, then other fields.
    print(start.time())
    print(end.time())
    student = Student.objects.get(net_id = name)
    student_entry = StudentEntry(
            net_id = name,
            entry_time = start,
            student = student, 
            end_time = end,
            requested_location = location
        )
    print('Before', StudentEntry.objects.count())

    student_entry.save()
    print('Student', StudentEntry.objects.count())

    # If this is a POST request then process the Form data
    # if request.method == 'POST':
    #     print("heyyyyyyyyyy")
    #     # Create a form instance and populate it with data from the request (binding):
    #     form = RequestAccessForm(request.POST)
    #     # key , value, location time,
    #     #take last location

    #     # Check if the form is valid:   
    #         # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
    #     student_entry.requested_location = form.cleaned_data['requested_location']
    #     student_entry.requested_time = form.cleaned_data['requested_time']
        
    #     #save ti redus
    #     #qr-> db, not present then insert, if present, then authorized = true, a
    #     # authorized 
    #         # if authorized then don't save, else save;
    #         # reading 
    #         # directly write a query with \timing 
            
    #     student_entry.save()

    #         # redirect to a new URL:
    #     return HttpResponseRedirect(reverse('') )
    # else:
    #     proposed_date = datetime.date.today() + datetime.timedelta(days=3)
    #     form = RequestAccessForm(initial={'requested_location': 'Bobst','requested_time':proposed_date })
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


def myview(request):
    # Build context for rendering QR codes.
    


    

    return render(request, 'home/index.html', {'form': form, 'student_entry':student_entry}, context=context)
    

# class AuthorizePage(forms.Form):
#     entry_requ
