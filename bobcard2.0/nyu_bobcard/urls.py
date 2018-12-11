from django.urls import path
from django.conf.urls import include, url
from qr_code import urls as qr_code_urls

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
	path('code/', views.request_access, name='code'), 
    path('authorize/<uuid:location_id>/<str:netid>', views.scanned_qr, name = 'authorize'),
]
