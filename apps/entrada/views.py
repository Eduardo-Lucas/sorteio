from django.shortcuts import render


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

