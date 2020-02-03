from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'my_users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='my_users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='my_users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
