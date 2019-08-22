from django.shortcuts import render


def home(request):
    return render(request, 'entrada/index.html')


def como_participar(request):
    return render(request, 'entrada/como_participar.html')


def premio(request):
    return render(request, 'entrada/premio.html')
