from django.contrib import admin
from .models import Lesson, Classroom


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "classroom",
        "start_time",
        "end_time",
        "teacher",
        "is_active",
    ]
    list_display_links = [
        "title",
    ]


admin.site.register(Classroom)
