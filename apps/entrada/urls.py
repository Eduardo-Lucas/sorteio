from django.urls import path

from apps.entrada.views import home

urlpatterns = [
    path('', home, name='home'),
    
]
