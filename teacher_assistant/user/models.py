from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    class Meta:
        verbose_name = "Teacher"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_info = models.TextField(max_length=500, blank=True)


class Student(models.Model):
    class Meta:
        verbose_name = "Student"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(
        Teacher,
    )

    def __str__(self):
        return f"User: {self.user}"
