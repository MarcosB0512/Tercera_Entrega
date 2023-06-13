from django import forms
import datetime

class FormularioCurso(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()
    fecha_create = forms.DateTimeField(initial=datetime.datetime.now, required=False, widget=forms.HiddenInput)
    fecha_update = forms.DateTimeField(initial=datetime.datetime.now, required=False, widget=forms.HiddenInput)


class FormularioProfesor(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    fecha_alta = forms.DateTimeField(initial=datetime.datetime.now, required=False, widget=forms.HiddenInput)

class FormularioEstudiante(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    fecha_alta = forms.DateTimeField(initial=datetime.datetime.now, required=False, widget=forms.HiddenInput)

class FormularioEntregable(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    fecha_alta = forms.DateTimeField(initial=datetime.datetime.now, required=False, widget=forms.HiddenInput)

