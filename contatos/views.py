from django.shortcuts import render
from .models import Contato


def index(request):
    return render(request, "contatos/index.html", {
        "contatos": Contato.objects.all()
    })


def ver_contato(request, contato_id):
    return render(request, "contatos/ver_contato.html", {
        "contato": Contato.objects.get(id=contato_id)
    })
