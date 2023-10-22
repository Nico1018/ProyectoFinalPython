from django.urls import path
from AppVeterinaria import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # ------------------about----------------------#
    path("about/", views.about, name="About"),
    # -----------------------animales-----------------------#
    path("animal/", views.animal, name="mascotas"),
    path(
        "apianimalform/",
        views.apiFormularioAnimal,
        name="FormularioAnimal",
    ),
    path("listaAnimales/", views.lista_animales, name="ListaAnimales"),
    path(
        "eliminar-animal/<int:animal_id>/",
        views.eliminar_animal,
        name="EliminarAnimal",
    ),
    path(
        "editar-animal/<int:animal_id>/",
        views.editar_animal,
        name="EditarAnimal",
    ),
    # ------------------------dueños-------------------------#
    path("persona/", views.persona, name="personas"),
    path(
        "apipersonaform/",
        views.apiFormularioPersona,
        name="ApiPersonaFormulario",
    ),
    path("listaPersonas/", views.lista_personas, name="ListaPersonas"),
    path(
        "eliminar-persona/<int:persona_id>/",
        views.eliminar_persona,
        name="EliminarPersona",
    ),
    path(
        "editar-persona/<int:persona_id>/",
        views.editar_persona,
        name="EditarPersona",
    ),
    # -------------------------inicio------------------------#
    path("", views.inicio, name="inicio"),
    # -----------------------------veterinario-------------------#
    path("veterinario/", views.veterinario, name="veterinarios"),
    path(
        "apiveterinarioform/",
        views.apiFormularioVeterinario,
        name="apiveterinarioformulario",
    ),
    path("listaVeterinarios/", views.lista_veterinarios, name="ListaVeterinarios"),
    path(
        "eliminar-veterinario/<int:veterinario_id>/",
        views.eliminar_veterinario,
        name="EliminarVeterinario",
    ),
    path(
        "editar-veterinario/<int:veterinario_id>/",
        views.editar_veterinario,
        name="EditarVeterinario",
    ),
    # --------------------login, register and logout-------------------
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path(
        "logout",
        LogoutView.as_view(template_name="AppVeterinaria/logout.html"),
        name="Logout",
    ),
]
