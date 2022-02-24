from django.urls import path
from django.contrib.auth import views as auth_views
from .views import landing, sign_up, logout_view

urlpatterns = [
    path('', landing, name='landing-home'),
    path('sign-up/', sign_up, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', logout_view, name='logout')
]


