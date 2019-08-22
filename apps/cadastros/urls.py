from django.urls import path

from apps.cadastros.views import CadastroListView, CadastroDetailView, CadastroCreateView, CadastroUpdateView, \
    CadastroDeleteView

urlpatterns = [
    
    path('list', CadastroListView.as_view(), name='cadastro_list'),
    path('detail/<int:pk>', CadastroDetailView.as_view(), name='cadastro_detail'),
    path('create', CadastroCreateView.as_view(), name='cadastro_create'),
    path('edit/<int:pk>', CadastroUpdateView.as_view(), name='cadastro_edit'),
    path('delete/<int:pk>', CadastroDeleteView.as_view(), name='cadastro_delete'),
    
]
