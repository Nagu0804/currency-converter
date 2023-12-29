from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('signup/', views.signup, name="signup"),    
    
    path('password_reset/', views.CustomPasswordResetFormView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="index/recovery/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="index/recovery/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="index/recovery/password_reset_complete.html"), name='password_reset_complete'),
    
    path('profile/', views.profile, name='profile'),
]
