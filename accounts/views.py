from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != "POST":
        return render(request, "accounts/login.html")

    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, "Usuário ou senhas inválidos")
        return render(request, "accounts/login.html")
    else:
        auth.login(request, user)
        messages.success(request, "Usuário logado")
        return redirect("dashboard")


def logout(request):
    auth.logout(request)
    return redirect("index")


def cadastro(request):
    if request.method != "POST":
        return render(request, "accounts/cadastro.html")

    email = request.POST.get("email")
    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")
    repita_senha = request.POST.get("repita_senha")

    if not email or not nome or not sobrenome \
            or not usuario or not senha or not repita_senha:
        messages.error(request, "Nenhum campo pode estar vazio")
        return render(request, "accounts/cadastro.html")

    try:
        validate_email(email)
    except:
        messages.error(request, "E-mail inválido")
        return render(request, "accounts/cadastro.html")

    if len(senha) < 6:
        messages.error(request, "Senha deve conter mais de 6 caracteres")
        return render(request, "accounts/cadastro.html")

    if len(usuario) < 6:
        messages.error(request, "Usuário deve conter mais de 6 caracteres")
        return render(request, "accounts/cadastro.html")

    if senha != repita_senha:
        messages.error(request, "Senhas devem ser iguais")
        return render(request, "accounts/cadastro.html")

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Usuario já existe")
        return render(request, "accounts/cadastro.html")

    if User.objects.filter(email=email).exists():
        messages.error(request, "E-mail já existe")
        return render(request, "accounts/cadastro.html")

    messages.success(request, "Usuário registrado com sucesso! Faça login!")

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect("login")


@login_required(redirect_field_name="login")
def dashboard(request):
    return render(request, "accounts/dashboard.html")
