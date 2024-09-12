from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    editar_perfil,
    login_custom_view,
    logout_custom_view,
    #change_password,
    #password_reset,
    #password_reset_confirm,

)

app_name = 'app.accounts'

urlpatterns = [
    path('login/', login_custom_view , name='login'),
    path('logout/', logout_custom_view, name='logout'),
    #path('update-password/', change_password , name='update-password'),
    #path('recover/', password_reset, name='recover'),
    #path('allowed-new-password/<key>',password_reset_confirm, name='allowed-new-password'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
