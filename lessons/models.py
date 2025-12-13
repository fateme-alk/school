from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Classroom(models.Model):
    name = models.CharField(max_length=10)
    is_usable = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize()


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
    )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title.capitalize()
