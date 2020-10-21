from django.urls import path

from imparh.core.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
