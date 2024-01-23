from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='reset.html'), name='reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_done.html'), name='reset_done'),
    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='reset_confirm'),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name='reset_complete'),
    path('accounts/profile/', views.profile, name='profile'),
]
