from django.urls import path

from suri.views import *

app_name='nothing'

urlpatterns=[
    
    path('CSK/',CSK,name='CSK'),
]