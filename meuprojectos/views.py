from django.shortcuts import render

def index(request):
    """Pagina principal de meuprojeto"""
    return render(request, 'meuprojectos/index.html')

def topics(request):
    """Mostra todos os assuntos"""