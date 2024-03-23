from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    DoesNotExist = None
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=300, verbose_name='ФИО', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
