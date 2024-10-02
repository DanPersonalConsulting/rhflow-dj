from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    editar_perfil,
    update_avatar,
    login_custom_view,
    logout_custom_view,
    CustomPasswordResetCompleteView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    #change_password,
    #password_reset,
    #password_reset_confirm,

)

app_name = 'app.account'

urlpatterns = [
    path('', login_custom_view , name='login'),
    path('logout/', logout_custom_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    #path('update-password/', change_password , name='update-password'),
    #path('recover/', password_reset, name='recover'),
    #path('allowed-new-password/<key>',password_reset_confirm, name='allowed-new-password'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('update_avatar/<int:user_id>', update_avatar, name='update_avatar'),

]
