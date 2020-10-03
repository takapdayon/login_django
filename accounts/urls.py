
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    Home
)

app_name = 'accounts'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]