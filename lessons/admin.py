from django.contrib import admin
from .models import Lesson, Classroom


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "classroom",
        "start_time",
        "end_time",
        "teacher",
        "is_active",
    )
    list_display_links = ("title",)
    list_filter = (
        "classroom",
        "start_time",
        "end_time",
        "teacher",
        "is_active",
    )
    search_fields = (
        "title",
        "classroom__name",
        "teacher__username",
        "is_active",
    )


@admin.register(Classroom)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_usable",
    )
