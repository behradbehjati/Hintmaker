from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns=[

   path('register/',views.RegisterView.as_view(),name='register'),
   path('login/',views.LoginView.as_view(),name='login'),
   path('logout/',views.LogoutView.as_view(),name='logout'),
   path('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),name='password_change'),
   path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
   path('password_reset/',views.PasswordResetView.as_view(),name='password_reset_view'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/email/password_reset_done.html'),name='password_reset_done'),
   path('password_reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('password_reset/MQ/set-password/password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/email/password_reset_complete.html'),name='password_reset_complete'),
   path('profile/',views.ProfileView.as_view(),name='profile'),
   path('profile_edit/',views.ProfileEditView.as_view(),name='profile_edit'),
   #path('login/',views.N_LoginView.as_view(),name='login' ),


]