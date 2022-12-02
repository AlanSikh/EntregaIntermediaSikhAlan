from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso,Alumno,Profesor
from django.core import serializers

from AppCoder.forms import CursoFormularios,PersonaFormularios

# Create your views here.
def Cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormularios(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(curso=informacion["curso"], camada=informacion["camada"], numero_dia=informacion["numero_dia"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario = CursoFormularios()
            
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})
def Alumnos(request):
    if request.method == "POST":
        miFormulario = PersonaFormularios(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno = Alumno(nombre=informacion["nombre"], email=informacion["email"], DNI=informacion["DNI"])
            alumno.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario = PersonaFormularios()
            
    return render(request, "AppCoder/Alumno.html", {"miFormulario": miFormulario})

def Profesores(request):
    if request.method == "POST":
        miFormulario = PersonaFormularios(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], email=informacion["email"], DNI=informacion["DNI"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario = PersonaFormularios()
            
    return render(request, "AppCoder/Profesor.html", {"miFormulario": miFormulario})

def Inicio(request):
    return render(request, "AppCoder/inicio.html")

def Cursosapi(request):
    cursos_todos = Curso.objects.all()
    print(cursos_todos)
    return HttpResponse(serializers.serialize('json',cursos_todos))

def VerCursos(request):

      cursos = Curso.objects.all() #trae todos los profesores

      contexto= {"cursos":cursos} 

      return render(request, "AppCoder/vercursos.html",contexto)

def Buscar(request):
    if  request.GET["camada"]:
        camada = request.GET['camada'] 
        cursos = Curso.objects.filter(camada__icontains=camada)
        contexto= {"cursos":cursos}
        return render(request, "AppCoder/vercursos.html",contexto)
    else: 
        return HttpResponse("No enviaste datos")