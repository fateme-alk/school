# Create your views here.
from .models import Lesson
from django.shortcuts import render


def lesson_list(request):
    all_lessons = Lesson.objects.all()
    context = {
        "all_lessons": all_lessons,
    }
    return render(request, "lessons/lesson_list.html", context=context)


def active_lessons(request):
    active_lessons = Lesson.objects.filter(is_active=1)
    context = {
        "active_lessons": active_lessons,
    }
    return render(request, "lessons/active_lessons.html", context=context)
