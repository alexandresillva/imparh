from django.contrib import admin
from django.urls import path
import imparh.core.views

urlpatterns = [
    path('', imparh.core.views.home),
    path('admin/', admin.site.urls),
]
