from django.contrib import admin

from user.models import Student, Teacher


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ("user",)
    # list_display_links = ("user",)


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = "user", "payment_info"
