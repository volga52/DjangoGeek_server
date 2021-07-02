from datetime import timedelta
# import datetime

from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def is_activation_key_expired(self):
        if now() < self.activation_key_created + timedelta(hours=48):
            return False
        return True
