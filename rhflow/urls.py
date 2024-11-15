from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.base.urls', namespace='base')),
    path('', include('app.accounts.urls', namespace='account')),
    path('', include('app.empresa.urls', namespace='empresa')),
    path('funcionarios/', include('app.funcionario.urls', namespace='funcionario')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
