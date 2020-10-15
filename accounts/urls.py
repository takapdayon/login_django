
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    Home,
    PasswordChange,
    PasswordChangeDone,
)

app_name = 'accounts'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
]
