from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    # note to self has to not start with /
   # http://127.0.0.1:8000/home/hello/252ad920-3066-47f5-a576-f376388545f7
#    path('hello/<uuid:pk>', views.request_access, name='request-access')
	path('code/', views.request_access, name='code'), 
    ## TODO:: change int to uuid

]
