from django.urls import path
from .views import (
    empresa_list, empresa_create, empresa_update, empresa_delete,
    organizacao_list, organizacao_create, organizacao_update, organizacao_delete,
)
    

app_name='app.empresa'

urlpatterns = [
    path('empresas/list/', empresa_list, name='empresa_list'),        
    path('empresas/create/', empresa_create, name='empresa_create'), 
    path('empresas/<int:pk>/update/', empresa_update, name='empresa_update'),  
    path('empresas/<int:pk>/delete/', empresa_delete, name='empresa_delete'), 
    path('organizacoes/', organizacao_list, name='organizacao_list'),
    path('organizacoes/nova/', organizacao_create, name='organizacao_create'),
    path('organizacoes/editar/<int:pk>/', organizacao_update, name='organizacao_update'),
    path('organizacoes/deletar/<int:pk>/', organizacao_delete, name='organizacao_delete'),
]
