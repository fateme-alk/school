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
    # it only controls which columns are allowed to be sorted when you click the column header in the Django admin UI.
    sortable_by = (
        "title",
        "classroom",
    )
    ordering = ("title",)


@admin.register(Classroom)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_usable",
    )


# below line are tradictional way to write admin model
# class ClassroomAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#         "is_usable",
#     )
# admin.site.register(Classroom, ClassroomAdmin)
