from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', tweet_list, name='tweet_list'),
    path('create/', tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit', tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete', tweet_delete, name='tweet_delete'),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('change_password/', change_password, name='change_password'),
    path('change_password/success/', password_change_success, name='password_change_success'),
]
