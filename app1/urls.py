from app1.views import *
from django.urls import path

app_name = 'something'

urlpatterns = [
    path('nani/',nani,name='nani'),
    path('nani2/',nani2,name='nani2'),
    
    
]