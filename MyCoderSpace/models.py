from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from ckeditor_uploader.fields import RichTextUploadingField
=======
from ckeditor.fields import RichTextField
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
<<<<<<< HEAD
<<<<<<< HEAD
    cuerpo = RichTextUploadingField()
=======
    cuerpo = models.TextField()
    imagen = models.URLField(max_length=300)
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
=======
    cuerpo = RichTextField(verbose_name="Contenido")
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.URLField()
    
    def __str__(self):
        return self.titulo

    
