from django.urls import path
from imparh.candidatos.views import new, detail

app_name = 'candidatos'

urlpatterns = [
    path('', new, name='new'),
    path('<uuid:pk>/', detail, name='detail'),

]
