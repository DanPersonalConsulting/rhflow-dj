from django.urls import path
from .views import index_view, home_view

app_name = 'app.base'

urlpatterns = [
    path('', index_view , name='index'),
    path('home/', home_view , name='home'),
   
]
