from django.urls import path
from AppCoder import views

urlpatterns = [
    
    path("", views.inicio, name = "Inicio"),
    path("cursos/", views.CursoList.as_view(), name = "List"),
    path("cursos/create", views.CursoCreacion.as_view(), name = "Create"),
    path("cursos/detail/<int:pk>/", views.CursoDetalle.as_view(), name = "Detail"),
    path("cursos/update/<int:pk>/", views.CursoUpdate.as_view(), name = "Update"),
    path("cursos/delete/<int:pk>/", views.CursoDelete.as_view(), name = "Delete"),
    path("AppCoder/buscar/", views.buscar),

    path("profesores/", views.ProfeList.as_view(), name = "List_Profe"),
    path("profesores/create", views.ProfeCreacion.as_view(), name = "Create_Profe"),
    path("profesores/detail/<int:pk>/", views.ProfeDetalle.as_view(), name = "Detail_Profe"),
    path("profesores/update/<int:pk>/", views.ProfeUpdate.as_view(), name = "Update_Profe"),
    path("profesores/delete/<int:pk>/", views.ProfeDelete.as_view(), name = "Delete_Profe"),

    path("estudiantes/", views.EstList.as_view(), name = "List_Est"),
    path("estudiantes/create", views.EstCreacion.as_view(), name = "Create_Est"),
    path("estudiantes/detail/<int:pk>/", views.EstDetalle.as_view(), name = "Detail_Est"),
    path("estudiantes/update/<int:pk>/", views.EstUpdate.as_view(), name = "Update_Est"),
    path("estudiantes/delete/<int:pk>/", views.EstDelete.as_view(), name = "Delete_Est"),

    path("entregables/", views.Entrega.as_view(), name = "Entregables"),
    path("entregables/list", views.EntregaList.as_view(), name = "List_Entrega"),
    path("entregables/create/", views.EntregaCreacion.as_view(), name = "Create_Entrega"),
    path("entregables/detail/<int:pk>/", views.EntregaDetalle.as_view(), name = "Detail_Entrega"),
    path("entregables/update/<int:pk>/", views.EntregaUpdate.as_view(), name = "Update_Entrega"),
    path("entregables/delete/<int:pk>/", views.EntregaDelete.as_view(), name = "Delete_Entrega"),
   
]
