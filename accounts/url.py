from django.urls import path
from .views import login, logout, locked, register, dashboard, Reset_Password_Complete
from django.contrib.auth import views as auth_views
from accounts.form import EmailValidationPassword


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout , name='logout'),
    # path('perfil/<int:id>/', perfil_usuario, name='perfil_user'),
    path('locked/', locked , name='locked'),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(
        template_name='accounts_templates/password_reset.html',
        email_template_name='accounts_templates/email_template.html',
        form_class=EmailValidationPassword
        ), 
    name='reset_password'),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='accounts_templates/reset_password_sent.html'), 
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts_templates/password_reset_form.html'), 
     name='password_reset_confirm'),

    path('reset_password_complete/', Reset_Password_Complete, name='password_reset_complete'),
]