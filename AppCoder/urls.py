
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("comentarios/", comentarios, name="comentarios"),
    path("buscar/", buscar, name="buscar"),
    
]
