from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    students = models.ManyToManyField("core.User", through='TeacherStudent')

    def __str__(self):
        return self.username


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    is_star = models.BooleanField(default=False)
