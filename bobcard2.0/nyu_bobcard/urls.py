#from django.conf.urls import url
#from .views import view_books

# everything above this line is imports that I added for the tutorial: https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    # note to self has to not start with /
   # http://127.0.0.1:8000/home/hello/252ad920-3066-47f5-a576-f376388545f7
#    path('hello/<uuid:pk>', views.request_access, name='request-access')
	path('code/', views.request_access, name='code'), 
    ## TODO:: change int to uuid
	path('authorize/<slug:location>/<slug:net_id>/<slug:time>', views.authorize, name='authorize'), 
        #url(r'^$', view_books),

]
#http://127.0.0.1:8000/home/hello
# urlpatterns += [   
#     path('/hello', views.request_access, name='request-access'),
# ]

#ps auxw | grep runserver
