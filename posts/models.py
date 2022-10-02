from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PostModel(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Teacher")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Student")
    lesson_type = models.CharField(max_length=255)
    lesson_name = models.CharField(max_length=255)
    lesson_time = models.DateTimeField()
    payment_status = models.BooleanField(default=False)
    payment_due_to = models.DateField()

    def __str__(self):
        return f"{self.student} with {self.teacher} | {self.lesson_type} | {self.lesson_time}"

    def get_absolute_url(self):
        return reverse("PostsView")