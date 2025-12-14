# Create your views here.
from .models import Lesson
from django.shortcuts import render


def lesson_list(request):
    all_lessons = Lesson.objects.all()
    context = {
        "all_lessons": all_lessons,
    }
    return render(request, "lessons/lesson_list.html", context=context)
