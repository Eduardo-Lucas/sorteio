from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.entrada.forms import ContactForm


def home(request):
    return render(request, 'entrada/index.html')


def como_participar(request):
    return render(request, 'entrada/como_participar.html')


def premio(request):
    return render(request, 'entrada/premio.html')


def regulamento(request):
    return render(request, 'entrada/regulamento.html')


def politica(request):
    return render(request, 'entrada/politica.html')


def duvidas(request):
    return render(request, 'entrada/duvidas.html')


def contato(request):
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nome_completo = form.cleaned_data['nome_completo']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            try:
                send_mail(nome_completo, mensagem, email, ['eduardolucas40@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
            
    return render(request, 'entrada/contato.html', {'form': form})


def successView(request):
    messages.add_message(request, messages.SUCCESS, 'Sucesso! Obrigado por sua mensagem.')
    form = ContactForm
    return render(request, 'entrada/contato.html', {'form': form})

