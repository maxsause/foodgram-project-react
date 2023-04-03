from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class UserFoodgram(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='Почта',
        blank=False,
        unique=True,
    )
    username = models.CharField(
        validators=(validate_username,),
        max_length=150,
        verbose_name='Никнейм',
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        blank=False,
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=False,
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль',
        blank=False,
    )
