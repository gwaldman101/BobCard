from django.shortcuts import render
from .models import Student, StudentEntry
from django.views import generic
from django import forms
from django.shortcuts import get_object_or_404
import datetime
# Create your views here.
from .forms import RequestAccessForm
def index(request):
    """View function for home page of site."""
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

def request_access(request, pk):
    """View function for renewing a specific StudentEntry by librarian."""
    student_entry = get_object_or_404(StudentEntry, pk = pk)
    
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RequestAccessForm(request.POST)
        # key , value, location time,
        #take last location

        # Check if the form is valid:   
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        student_entry.requested_location = form.cleaned_data['requested_location']
        student_entry.requested_time = form.cleaned_data['requested_time']
        
        #save ti redus
        #qr-> db, not present then insert, if present, then authorized = true, a
        # authorized 
            # if authorized then don't save, else save;
            # reading 
            # directly write a query with \timing 
            
        student_entry.save()

            # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )
    else:
        proposed_date = datetime.date.today() + datetime.timedelta(days=3)
        form = RequestAccessForm(initial={'requested_location': 'Bobst','requested_time':proposed_date })


    # If this is a GET (or any other method) create the default form
    
    context = {
        'form': form,
        'student_entry': student_entry,
    }

    return render(request, 'home/request_access.html', {'form': form, 'student_entry':student_entry})
    

# class AuthorizePage(forms.Form):
#     entry_requ