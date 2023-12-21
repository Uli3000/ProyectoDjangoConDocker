from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class  UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null = True, blank=True)
    # Añadir 'related_name' a las relaciones muchos a muchos
UsuarioPers._meta.get_field('groups').related_name = 'usuario_pers_groups'
UsuarioPers._meta.get_field('user_permissions').related_name = 'usuario_pers_user_permissions'
User._meta.get_field('groups').related_name = 'auth_user_groups'
User._meta.get_field('user_permissions').related_name = 'auth_user_user_permissions'