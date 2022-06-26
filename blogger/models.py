<<<<<<< HEAD
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80


<<<<<<< HEAD
=======
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80
