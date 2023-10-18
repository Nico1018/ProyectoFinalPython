from django.urls import path
from AppVeterinaria import views

urlpatterns = [
    path("animal/", views.animal, name="mascotas"),
    path("veterinario/", views.veterinario, name="veterinarios"),
    path("persona/", views.persona, name="personas"),
    path("", views.inicio, name="inicio"),
    path("form/", views.formularioVeterinario, name="formulario"),
]
