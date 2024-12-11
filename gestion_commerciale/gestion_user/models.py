# gestion_user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=[('admin', 'Admin'), ('user', 'User')],
        default='user',  # Valeur par défaut pour le rôle
    )
    class Meta:
        db_table = 'CustomUser'
