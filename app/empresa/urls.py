from django.urls import path
from .views import (
    empresa_list, empresa_create, empresa_update, empresa_delete,
    organizacao_list, organizacao_create, organizacao_update, organizacao_delete,
    gestor_rh_list, gestor_rh_create, gestor_rh_delete, gestor_rh_update,
)
    

app_name='app.empresa'

urlpatterns = [
    path('empresas/list/', empresa_list, name='empresa_list'),        
    path('empresas/novo/', empresa_create, name='empresa_create'), 
    path('empresas/editar/<int:pk>', empresa_update, name='empresa_update'),  
    path('empresas/delete/<int:pk>', empresa_delete, name='empresa_delete'), 
    path('organizacoes/list/', organizacao_list, name='organizacao_list'),
    path('organizacoes/novo/', organizacao_create, name='organizacao_create'),
    path('organizacoes/editar/<int:pk>', organizacao_update, name='organizacao_update'),
    path('organizacoes/deletar/<int:pk>', organizacao_delete, name='organizacao_delete'),
    path('gestores/list/', gestor_rh_list, name='gestor_rh_list'),
    path('gestores/novo/', gestor_rh_create, name='gestor_rh_create'),
    path('gestores/editar/<int:pk>', gestor_rh_update, name='gestor_rh_update'),
    path('gestores/deletar/<int:pk>', gestor_rh_delete, name='gestor_rh_delete'),
]
