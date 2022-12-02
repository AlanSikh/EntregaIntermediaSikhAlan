from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.Inicio, name="Inicio"),
    path('cursos/', views.Cursos, name="Cursos"),
    path('cursos/lista', views.VerCursos, name="CursosLista"),
    path('cursosApi/', views.Cursosapi),
    path("profesor/",views.Profesores, name="Profesor"),
    path("alumnos/",views.Alumnos, name="Alumnos"),
    path("buscar/",views.Buscar, name="Buscar"),
]