from django.shortcuts import render
from AppVeterinaria.models import Veterinario
from AppVeterinaria.forms import VeterinarioFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


# ------------------animal-----------------------------#
@login_required
def animal(request):
    return render(request, "AppVeterinaria/animal.html")


# ------------------persona----------------------------#
@login_required
def persona(request):
    return render(request, "AppVeterinaria/persona.html")


# ------------------inicio--------------------------#
@login_required
def inicio(request):
    return render(request, "AppVeterinaria/index.html")


# ---------------veterinario-------------------#
@login_required
def veterinario(request):
    return render(request, "AppVeterinaria/veterinario.html")


def apiFormularioVeterinario(request):
    if request.method == "POST":
        miFormulario = VeterinarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            veterinario = Veterinario(
                nombre_vet=informacion["nombre_vet"],
                apellido_vet=informacion["apellido_vet"],
                matricula=informacion["matricula"],
            )
            veterinario.save()
            return render(request, "AppVeterinaria/index.html")
    else:
        miFormulario = VeterinarioFormulario()

    return render(
        request,
        "AppVeterinaria/apiveterinarioformulario.html",
        {"miFormulario": miFormulario},
    )


def read_comun(request):
    veterinarios = Veterinario.objects.all()
    return render(
        request, "AppVeterinaria/read_comun.html", {"veterinarios": veterinarios}
    )


def delete_comun(request, veterinario_id):
    veterinario = Veterinario.objects.get(id=veterinario_id)
    veterinario.delete()

    return read_comun(request)


def edit_comun(request, veterinario_id):
    if request.method == "POST":
        miFormulario = VeterinarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            veterinario = Veterinario.objects.get(id=veterinario_id)
            veterinario.nombre_vet = informacion["nombre_vet"]
            veterinario.apellido_vet = informacion["apellido_vet"]
            veterinario.matricula = informacion["matricula"]
            veterinario.save()

            return render(request, "AppVeterinaria/index.html")
    else:
        veterinario = Veterinario.objects.get(id=veterinario_id)
        miFormulario = VeterinarioFormulario(
            initial={
                "nombre_vet": veterinario.nombre_vet,
                "apellido_vet": veterinario.apellido_vet,
                "matricula": veterinario.matricula,
            }
        )

    return render(
        request,
        "AppVeterinaria/apiveterinarioformulario.html",
        {"miFormulario": miFormulario},
    )


# -------------------Login-----------------#
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(
                    request,
                    "AppVeterinaria/base NavYFoot.html",
                    {"mensaje": f"Bienvenido {usuario}"},
                )
            else:
                return render(
                    request,
                    "AppVeterinaria/base NavYFoot.html",
                    {"mensaje": "Datos incorrectos"},
                )

        else:
            return render(
                request,
                "AppVeterinaria/base NavYFoot.html",
                {"mensaje": "Formulario erroneo"},
            )

    form = AuthenticationForm()

    return render(request, "AppVeterinaria/login.html", {"form": form})


# --------------register------------------------


def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(
                request,
                "AppVeterinaria/base NavYFoot.html",
                {"mensaje": "Usuario Creado :)"},
            )

    else:
        # form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppVeterinaria/register.html", {"form": form})
