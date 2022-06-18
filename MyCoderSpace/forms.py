from django import forms

class CrearBlog(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Titulo'}))
    subtitulo = forms.CharField(label="Subtitulo", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subtitulo'}))
    cuerpo = forms.CharField(label="Cuerpo", max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Escribe tu Blog'}))