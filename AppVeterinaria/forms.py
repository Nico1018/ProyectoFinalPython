from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VeterinarioFormulario(forms.Form):
    nombre_vet = forms.CharField(max_length=20)
    apellido_vet = forms.CharField(max_length=30)
    matricula = forms.CharField(max_length=20)


class AnimalFormulario(forms.Form):
    nombreAnimal = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    tipo = forms.CharField(max_length=40)
    motivo = forms.CharField(max_length=40)
    fecha = forms.DateField()
    costo = forms.IntegerField()


class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    telefono = forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
