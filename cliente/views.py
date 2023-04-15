from django.shortcuts import render
from eventos.models import Certificado, Evento
from django.contrib.auth.decorators import login_required

@login_required
def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados':certificados})

@login_required
def meus_eventos(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        eventos = Evento.objects.filter(participantes=request.user)

        if nome:
            eventos = eventos.filter(nome__contains=nome)

        return(render(request, 'meus_eventos.html', {'eventos':eventos}))