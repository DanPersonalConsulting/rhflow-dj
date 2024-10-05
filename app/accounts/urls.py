from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .views import (
    editar_perfil,
    update_avatar,
    login_custom_view,
    logout_custom_view,
    CustomPasswordResetCompleteView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    CustomPasswordChangeView,
)

app_name = 'app.account'

urlpatterns = [
    path('', login_custom_view , name='login'),
    path('logout/', logout_custom_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('change_password/', CustomPasswordChangeView.as_view(template_name='registration/password_change.html'), name='change_password'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('update_avatar/<int:user_id>', update_avatar, name='update_avatar'),

]
