from django.db import models

class Blogger(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Avatar(models.Model):
    usuario = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)