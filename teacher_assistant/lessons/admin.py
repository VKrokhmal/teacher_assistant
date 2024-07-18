from django.contrib import admin

from lessons.models import Lesson, Series


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ["name", "teacher", "price", "currency", "lesson_time"]


@admin.register(Series)
class LessonSeries(admin.ModelAdmin):
    list_display = ["lesson", "student", "day_of_week", "time", "created_datetime"]
