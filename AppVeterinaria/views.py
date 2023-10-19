from django.shortcuts import render
from django.http import HttpResponse
from AppVeterinaria.models import Veterinario

# Create your views here.


def animal(request):
    return render(request, "AppVeterinaria/animal.html")


def veterinario(request):
    return render(request, "AppVeterinaria/veterinario.html")


def persona(request):
    return render(request, "AppVeterinaria/persona.html")


def inicio(request):
    return render(request, "AppVeterinaria/index.html")


def formularioVeterinario(request):
    if request.method == "POST":
        mi_formulario_veterinario = Veterinario(
            nombre_vet=request.POST["nombre_vet"],
            apellido_Vet=request.POST["apellido_Vet"],
            matricula=request.POST["matricula"],
        )

        mi_formulario_veterinario.save()

        return render(request, "AppVeterinaria/index.html")

    return render(request, "AppVeterinaria/veterinarioformulario.html")
