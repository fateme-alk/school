from django.urls import path
from .views import lesson_list, active_lessons

urlpatterns = [
    path("all/", lesson_list),
    path("active/", active_lessons),
]
