from django.urls import path
from .views import ocean

urlpatterns = [

    path('', ocean, name='bottles-home'),
   
]