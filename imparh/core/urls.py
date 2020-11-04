from django.urls import path

from imparh.core.views import home

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
]
