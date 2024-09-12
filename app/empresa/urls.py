from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
   nova_empresa_view,

)

app_name = 'app.empresa'

urlpatterns = [
    path('nova_empresa/', nova_empresa_view, name='empresa'),
]
