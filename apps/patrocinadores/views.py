from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from apps.patrocinadores.models import Patrocinador


class PatrocinadorListView(ListView):
    model = Patrocinador
    fields = ['nome', 'logo', 'ativo', ]
    template_name = 'patrocinadores/patrocinador_list.html'
    
    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(nome__icontains=valor) |
                Q(id__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()
        
        paginator = Paginator(object_list, 10)
        
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)
        
        # return object_list
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(PatrocinadorListView, self).get_context_data(**kwargs)
        context['count'] = Patrocinador.objects.count()
        return context


class PatrocinadorDetailView(DetailView):
    model = Patrocinador


class PatrocinadorCreateView(SuccessMessageMixin, CreateView):
    model = Patrocinador
    fields = ['nome', 'logo', ]
    success_message = 'O patrocinador de %(nome)s foi realizado com sucesso.'
    

class PatrocinadorUpdateView(SuccessMessageMixin, UpdateView):
    model = Patrocinador
    fields = ['nome', 'logo', ]
    success_message = 'O patrocinador de %(nome)s foi alterado com sucesso.'


class PatrocinadorDeleteView(DeleteView):
    model = Patrocinador
    success_url = reverse_lazy('patrocinador_list')

