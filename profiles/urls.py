from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profile'),
    path('inbox/', views.inbox.as_view(), name='inbox')
]