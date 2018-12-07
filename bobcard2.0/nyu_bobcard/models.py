from django.db import models
# Create your models here.
from datetime import datetime    
# To generate URLS by reversing URL patterns
from django.urls import reverse  
import uuid  # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower

class StudentEntry(models.Model):
    # need a primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student = models.ForeignKey("Student", on_delete=models.CASCADE) # if student gets deleted we delete this as well
    entry_time = models.DateTimeField(default=datetime.now, blank=True)
    requested_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    requested_location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True) # should this be like a foreign field?

    class Meta:
        ordering = ['entry_time'] # ordering should be by eviction?
       # permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.student, self.requested_location)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000) 
    location = models.ManyToManyField("Location")

    #net_id = models.CharField(max_length=50, primary_key=True) # unique enuf

    def __str__(self):
        return self.name

class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


//bobcard/student_id/location/time-requested