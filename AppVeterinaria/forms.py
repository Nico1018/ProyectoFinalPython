from django import forms


class VeterinarioFormulario(forms.Form):
    nombre_vet = forms.CharField(max_length=20)
    apellido_vet = forms.CharField(max_length=30)
    matricula = forms.CharField(max_length=20)
