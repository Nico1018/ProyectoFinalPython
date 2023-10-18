from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def animal(request):
    return render(request, "AppVeterinaria/animal.html")


def veterinario(request):
    return render(request, "AppVeterinaria/veterinario.html")


def persona(request):
    return render(request, "AppVeterinaria/persona.html")


def inicio(request):
    return render(request, "AppVeterinaria/index.html")
