from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    class Meta:
        verbose_name = "Teacher"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_info = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"Teacher: {self.user}"


class Student(models.Model):
    class Meta:
        verbose_name = "Student"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_info = models.ManyToManyField(
        Teacher,
    )

    def __str__(self):
        return f"Student: {self.user}"
