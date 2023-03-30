from django.shortcuts import render, get_object_or_404
from .models import Contato


def index(request):
    return render(request, "contatos/index.html", {
        "contatos": Contato.objects.all()
    })


def ver_contato(request, contato_id):
    return render(request, "contatos/ver_contato.html", {
        "contato": get_object_or_404(Contato, id=contato_id)
    })
