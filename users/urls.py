from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verification_user, password_recovery

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('success_register/<str:register_uuid>/', verification_user, name='success_register'),
    path('password_recovery', password_recovery, name='password_recovery'),
    path('profile/', ProfileView.as_view(), name='profile'),
]