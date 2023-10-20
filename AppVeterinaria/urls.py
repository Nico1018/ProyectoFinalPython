from django.urls import path
from AppVeterinaria import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("animal/", views.animal, name="mascotas"),
    path("veterinario/", views.veterinario, name="veterinarios"),
    path("persona/", views.persona, name="personas"),
    path("", views.inicio, name="inicio"),
    path(
        "apiveterinarioform/",
        views.apiFormularioVeterinario,
        name="apiveterinarioformulario",
    ),
    path("read_comun/", views.read_comun, name="ReadComun"),
    path(
        "eliminar-veterinario/<int:veterinario_id>/",
        views.delete_comun,
        name="EliminarVeterinario",
    ),
    path(
        "editar-veterinario/<int:veterinario_id>/",
        views.edit_comun,
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
