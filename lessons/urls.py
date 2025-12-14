from django.urls import path
from .views import lesson_list

urlpatterns = [
    path("all/", lesson_list),
]
