from django.urls import path
from .views import funcionario_list, funcionario_create, funcionario_update, funcionario_delete

app_name = 'app.funcionario'

urlpatterns = [
    path('list/', funcionario_list, name='funcionario_list'),        
    path('create/', funcionario_create, name='funcionario_create'),  
    path('<int:pk>/update/', funcionario_update, name='funcionario_update'),
    path('<int:pk>/delete/', funcionario_delete, name='funcionario_delete'), 
]