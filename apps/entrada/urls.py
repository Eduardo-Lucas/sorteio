from django.urls import path

from apps.entrada.views import home, como_participar, premio, regulamento, politica

urlpatterns = [
    path('', home, name='home'),
    path('como_participar', como_participar, name='como_participar'),
    path('premio', premio, name='premio'),
    path('regulamento', regulamento, name='regulamento'),
    path('politica', politica, name='politica'),
    
]
