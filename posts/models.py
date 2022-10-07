from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from server import settings


DAYS_OF_WEEK = (
    ("0", 'Monday'),
    ("1", 'Tuesday'),
    ("2", 'Wednesday'),
    ("3", 'Thursday'),
    ("4", 'Friday'),
    ("5", 'Saturday'),
    ("6", 'Sunday'),
)


class PostModel(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Teacher")
    lesson_type = models.CharField(max_length=255)
    lesson_name = models.CharField(max_length=255)
    lesson_week = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    lesson_time = models.TimeField()
    payment_status = models.BooleanField(default=False)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return f"{self.students} with {self.teacher} | {self.lesson_type} | {self.lesson_time}"

    def get_absolute_url(self):
        return reverse("PostsView")

