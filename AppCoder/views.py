from django.shortcuts import render
from .models import Usuarios, Comentarios
from django.http import HttpResponse

from AppCoder.forms import UsuariosForm, ComentariosForm, BuscarForm
# Create your views here.

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def usuarios(request):
    if request.method=="POST":
        form=UsuariosForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre =informacion["nombre"]
            apellido = informacion["apellido"]
            dni = informacion["dni"]
            fecha_nacimiento = informacion["fecha_nacimiento"]
            password = informacion["password"]
            email = informacion["email"]
            curso=Usuarios(nombre=nombre, apellido=apellido,dni=dni,fecha_nacimiento=fecha_nacimiento,password=password,email=email)
            curso.save()
            return render (request, "Appcoder/inicio.html", {"mensaje":"Se ha creado el usuario"})


    else:
        formulario=UsuariosForm()
        return render (request, "AppCoder/usuarios.html", {"formulario":formulario})


def comentarios(request):

    if request.method=="POST":
        form= ComentariosForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            titulo = informacion['titulo']
            comentario = informacion['comentario']
            fecha = informacion['fecha']
            usuario = informacion['usuario']
            coment= Comentarios(titulo=titulo, comentario=comentario, fecha=fecha, usuario=usuario)
            coment.save()
            return render (request, "Appcoder/inicio.html", {"mensaje":"Se ha creado el comentario"})
    else:
        form= ComentariosForm()
    return render(request, "Appcoder/comentarios.html", {"formulario":form})

def buscar(request):

    if request.method=="POST":
        form= BuscarForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            cantidad = len(Comentarios.objects.filter(comentario=informacion['cadena']))
            return render(request, "Appcoder/resultadosBusqueda.html", {"cantidad":cantidad, "comentarios":Comentarios.objects.filter(comentario=informacion['cadena'])})
            
    else:
        form = BuscarForm()
        return render(request, "Appcoder/buscar.html", {"formulario":form})




    
    








