from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = RichTextField(verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.URLField()
    
    def __str__(self):
        return self.titulo

    
