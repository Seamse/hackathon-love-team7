from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profile'),
    path('inbox-detail/<slug:slug>/', views.InboxDetail.as_view(), name='inbox_detail'),
    path('inbox/', views.inbox.as_view(), name='inbox')
]

