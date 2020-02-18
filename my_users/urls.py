from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='my_users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='my_users/logout.html'), name='logout'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='my_users/password_reset.html'),
        name='password_reset'
    ),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='my_users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='my_users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='my_users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path('profile/', views.profile, name='profile'),
]
