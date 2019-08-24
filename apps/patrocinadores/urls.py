from django.urls import path

from apps.patrocinadores.views import PatrocinadorListView, PatrocinadorDetailView, PatrocinadorCreateView, \
    PatrocinadorUpdateView, PatrocinadorDeleteView

urlpatterns = [
    path('list', PatrocinadorListView.as_view(), name='patrocinador_list'),
    path('detail/<int:pk>', PatrocinadorDetailView.as_view(), name='patrocinador_detail'),
    path('create', PatrocinadorCreateView.as_view(), name='patrocinador_create'),
    path('edit/<int:pk>', PatrocinadorUpdateView.as_view(), name='patrocinador_edit'),
    path('delete/<int:pk>', PatrocinadorDeleteView.as_view(), name='patrocinador_delete'),
    
]
