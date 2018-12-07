from django.contrib import admin

# Register your models here.
from nyu_bobcard.models import Location, StudentEntry, Student

admin.site.register(Location)
admin.site.register(StudentEntry)
admin.site.register(Student)
