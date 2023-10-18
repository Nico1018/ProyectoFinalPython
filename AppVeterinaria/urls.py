from django.urls import path
from .views import animal, veterinario, persona, inicio

urlpatterns = [
    path("animal/", animal, name="mascotas"),
    path("veterinario/", veterinario, name="veterinarios"),
    path("persona/", persona, name="personas"),
    path("", inicio, name="inicio"),
]
