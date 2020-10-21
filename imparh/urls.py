from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('core/', include('imparh.core.urls')),
    path('admin/', admin.site.urls),
    path('candidatos/', include('imparh.candidatos.urls')),
]
