from django.urls import path
from app2.views import *

app_name = 'nothing'

urlpatterns = [
    path('sai/',sai,name='sai'),
    path('sai2/',sai2,name='sai2')
]