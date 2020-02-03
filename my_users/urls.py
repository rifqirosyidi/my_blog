from django.urls import path
from . import views

app_name = 'my_users'
urlpatterns = [
    path('register/', views.register, name='register'),
]
