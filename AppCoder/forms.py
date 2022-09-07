from django import forms

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    password = forms.CharField(max_length=10)
    email = forms.EmailField()
    
class ComentariosForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    comentario = forms.CharField(max_length=256)
    fecha = forms.DateField()
    usuario = forms.IntegerField()

class BuscarForm(forms.Form):
    cadena = forms.CharField(max_length=256)





    