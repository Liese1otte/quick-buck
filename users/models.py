from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPES = (
    ("0", "Teacher"),
    ("1", "Student"),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default="1")