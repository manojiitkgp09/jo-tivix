from django.db import models


from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    students = models.ManyToManyField(Student, through='TeacherStudent')

    def __str__(self):
        return self.username

    @property
    def name(self):
        full_name = f'{self.first_name} {self.last_name}'
        if not full_name.strip():
            return self.username
        return full_name


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return f'Teacher: {self.teacher.name}, Student: {self.student.name}'
