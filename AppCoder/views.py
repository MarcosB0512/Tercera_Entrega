from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Curso, Profesor, Estudiante, Entregable
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def buscar(request):

    if request.GET["camada"]:
               
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains = camada)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    
    else:         
        return render(request, "AppCoder/inicio.html", "No enviate datos") 

# cursos
class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    template_name = "AppCoder/curso_creacion.html"
    fields = ['nombre', 'camada']
    success_url = reverse_lazy('List')

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "AppCoder/curso_form.html"
    fields = ['nombre', 'camada']
    success_url = reverse_lazy('List')

class CursoDelete(DeleteView):
    model = Curso
    template_name = "AppCoder/curso_confirm_delete.html"
    success_url = reverse_lazy('List')

# profesores
class ProfeList(ListView):
    model = Profesor
    template_name = "AppCoder/profesores.html"

class ProfeDetalle(DetailView):
    model = Profesor
    template_name = "AppCoder/profe_detalle.html"

class ProfeCreacion(CreateView):
    model = Profesor
    template_name = "AppCoder/profe_creacion.html"
    fields = ['nombre', 'apellido', 'email', 'profesion']
    success_url = reverse_lazy('List_Profe')

class ProfeUpdate(UpdateView):
    model = Profesor
    template_name = "AppCoder/profe_form.html"
    fields = ['nombre', 'apellido', 'email', 'profesion']
    success_url = reverse_lazy('List_Profe')

class ProfeDelete(DeleteView):
    model = Profesor
    template_name = "AppCoder/profe_confirm_delete.html"
    success_url = reverse_lazy('List_Profe')

# estudiantes
class EstList(ListView):
    model = Estudiante
    template_name = "AppCoder/estudiantes.html"

class EstDetalle(DetailView):
    model = Estudiante
    template_name = "AppCoder/est_detalle.html"

class EstCreacion(CreateView):
    model = Estudiante
    template_name = "AppCoder/est_creacion.html"
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('List_Est')

class EstUpdate(UpdateView):
    model = Estudiante
    template_name = "AppCoder/est_form.html"
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('List_Est')

class EstDelete(DeleteView):
    model = Estudiante
    template_name = "AppCoder/est_confirm_delete.html"
    success_url = reverse_lazy('List_Est')

# entregables
class Entrega(ListView):
    model = Entregable
    template_name = "AppCoder/entregables.html"

class EntregaList(ListView):
    model = Entregable
    template_name = "AppCoder/entrega_list.html"

class EntregaCreacion(CreateView):
    model = Entregable
    template_name = "AppCoder/entregables.html"
    fields = ['nombre', 'fecha_de_Entrega', 'entregado']
    success_url = reverse_lazy('Entregables')

    def form_valid(self, form):
        form.instance.entregado = int(self.request.POST.get('entregado', '0'))
        return super().form_valid(form)

class EntregaDetalle(DetailView):
    model = Entregable
    template_name = "AppCoder/Entrega_detalle.html"

class EntregaUpdate(UpdateView):
    model = Entregable
    template_name = "AppCoder/Entrega_editar.html"
    fields = ['nombre', 'fecha_de_Entrega', 'entregado']
    success_url = reverse_lazy('List_Entrega')

class EntregaDelete(DeleteView):
    model = Entregable
    template_name = "AppCoder/Entrega_confirm_delete.html"
    success_url = reverse_lazy('List_Entrega')



    




