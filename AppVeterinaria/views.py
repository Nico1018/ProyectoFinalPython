from django.shortcuts import render
from AppVeterinaria.models import Veterinario, Animal, Persona, Avatar
from AppVeterinaria.forms import (
    VeterinarioFormulario,
    AnimalFormulario,
    PersonaFormulario,
    UserRegisterForm,
    UserEditForm,
)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


# ------------------animal-----------------------------#
@login_required
def animal(request):
    return render(request, "AppVeterinaria/animal.html")


@login_required
def apiFormularioAnimal(request):
    if request.method == "POST":
        miFormulario = AnimalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            animal = Animal(
                nombreAnimal=informacion["nombreAnimal"],
                edad=informacion["edad"],
                tipo=informacion["tipo"],
                motivo=informacion["motivo"],
                fecha=informacion["fecha"],
                costo=informacion["costo"],
            )
            animal.save()
            return render(request, "AppVeterinaria/index.html")
    else:
        miFormulario = AnimalFormulario()

    return render(
        request,
        "AppVeterinaria/apianimalformulario.html",
        {"miFormulario": miFormulario},
    )


@login_required
def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, "AppVeterinaria/listaAnimal.html", {"animales": animales})


@login_required
def eliminar_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    animal.delete()

    return lista_animales(request)


@login_required
def editar_animal(request, animal_id):
    if request.method == "POST":
        miFormulario = AnimalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            animal = Animal.objects.get(id=animal_id)
            animal.nombreAnimal = informacion["nombreAnimal"]
            animal.edad = informacion["edad"]
            animal.tipo = informacion["tipo"]
            animal.motivo = informacion["motivo"]
            animal.fecha = informacion["fecha"]
            animal.costo = informacion["costo"]
            animal.save()

            return render(request, "AppVeterinaria/index.html")
    else:
        animal = Animal.objects.get(id=animal_id)
        miFormulario = AnimalFormulario(
            initial={
                "nombreAnimal": animal.nombreAnimal,
                "edad": animal.edad,
                "tipo": animal.tipo,
            }
        )

    return render(
        request,
        "AppVeterinaria/apianimalformulario.html",
        {"miFormulario": miFormulario},
    )


# ------------------persona----------------------------#
@login_required
def persona(request):
    return render(request, "AppVeterinaria/persona.html")


@login_required
def apiFormularioPersona(request):
    if request.method == "POST":
        miFormulario = PersonaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            persona = Persona(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                telefono=informacion["telefono"],
                dni=informacion["dni"],
            )
            persona.save()
            return render(request, "AppVeterinaria/index.html")
    else:
        miFormulario = PersonaFormulario()

    return render(
        request,
        "AppVeterinaria/apipersonaformulario.html",
        {"miFormulario": miFormulario},
    )


@login_required
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, "AppVeterinaria/listapersonas.html", {"personas": personas})


@login_required
def eliminar_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    persona.delete()

    return lista_personas(request)


@login_required
def editar_persona(request, persona_id):
    if request.method == "POST":
        miFormulario = PersonaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            persona = Persona.objects.get(id=persona_id)
            persona.nombre = informacion["nombre"]
            persona.apellido = informacion["apellido"]
            persona.telefono = informacion["telefono"]
            persona.dni = informacion["dni"]
            persona.save()

            return render(request, "AppVeterinaria/index.html")
    else:
        persona = Persona.objects.get(id=persona_id)
        miFormulario = PersonaFormulario(
            initial={
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "telefono": persona.telefono,
                "dni": persona.dni,
            }
        )

    return render(
        request,
        "AppVeterinaria/apipersonaformulario.html",
        {"miFormulario": miFormulario},
    )


# ------------------inicio--------------------------#
@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user.id)[0]
    return render(request, "AppVeterinaria/index.html", {"url": avatar})


# ---------------veterinario-------------------#
@login_required
def veterinario(request):
    return render(request, "AppVeterinaria/veterinario.html")


@login_required
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
            return render(request, "AppVeterinaria/listaveterinarios.html")
    else:
        miFormulario = VeterinarioFormulario()

    return render(
        request,
        "AppVeterinaria/apiveterinarioformulario.html",
        {"miFormulario": miFormulario},
    )


@login_required
def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(
        request, "AppVeterinaria/listaveterinarios.html", {"veterinarios": veterinarios}
    )


@login_required
def eliminar_veterinario(request, veterinario_id):
    veterinario = Veterinario.objects.get(id=veterinario_id)
    veterinario.delete()

    return lista_veterinarios(request)


@login_required
def editar_veterinario(request, veterinario_id):
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


# ----------------------------about------------------#
def about(request):
    return render(request, "AppVeterinaria/about.html")


# ---------------------------edit user---------------#
@login_required
def edit(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]

            usuario.save()

            return render(request, "AppVeterinaria/index.html")

    else:
        datos = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "username": usuario.username,
            "last_name": usuario.last_name,
        }
        miFormulario = UserEditForm(initial=datos)

    return render(
        request,
        "AppVeterinaria/edit.html",
        {"mi_form": miFormulario, "usuario": usuario},
    )
