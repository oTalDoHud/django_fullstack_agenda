from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 1)

    page = request.GET.get("page")
    contatos = paginator.get_page(page)

    return render(request, "contatos/index.html", {
        "contatos": contatos
    })


def ver_contato(request, contato_id):
    return render(request, "contatos/ver_contato.html", {
        "contato": get_object_or_404(Contato, id=contato_id)
    })
