from django.urls import path
from . import views

urlpatterns = [
    path('', views.LetterList.as_view(), name='letter_list'),
    # path('<slug:slug>/', views.LetterDetail.as_view(), name='letter_detail'),
    path('letter-detail/<slug:slug>/', views.LetterDetail.as_view(), name='letter_detail'),
    path('contact/<slug:slug>/', views.ContactView, name="contact"),
]
