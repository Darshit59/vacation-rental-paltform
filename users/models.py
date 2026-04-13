from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('host', 'Host'),
        ('guest', 'Guest'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

    phone = models.CharField(max_length=15, blank=True, null=True)

    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)