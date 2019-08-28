from django.urls import path

from apps.entrada.views import home, como_participar, premio, regulamento, politica, duvidas, contato, successView

urlpatterns = [
    path('', home, name='home'),
    path('como_participar', como_participar, name='como_participar'),
    path('premio', premio, name='premio'),
    path('regulamento', regulamento, name='regulamento'),
    path('duvidas', duvidas, name='duvidas'),
    path('politica', politica, name='politica'),
    path('contato', contato, name='contato'),
    path('success', successView, name='success'),
    
]
