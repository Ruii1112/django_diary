from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name="id")
    email = models.EmailField(unique=True, verbose_name="メールアドレス")

    def __str__(self):
        return self.username