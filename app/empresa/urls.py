from django.urls import path
from .views import empresa_list, empresa_create, empresa_update, empresa_delete

app_name='app.empresa'

urlpatterns = [
    path('list/', empresa_list, name='empresa_list'),        
    path('create/', empresa_create, name='empresa_create'), 
    path('<int:pk>/update/', empresa_update, name='empresa_update'),  
    path('<int:pk>/delete/', empresa_delete, name='empresa_delete'), 
]
