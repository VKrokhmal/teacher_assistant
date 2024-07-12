from django.contrib import admin

from user.models import Student, Teacher


@admin.register(Student)
class Student(admin.ModelAdmin):
    pass
    # list_display = "user", "teacher_info"


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    # pass
    list_display = "user", "payment_info"
