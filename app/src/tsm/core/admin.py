from django.contrib import admin
from django.contrib.admin import register

from django.contrib.auth.admin import UserAdmin
from .models import User, Student, TeacherStudent


class StudentInline(admin.TabularInline):

    model = User.students.through
    verbose_name = u"Student"
    verbose_name_plural = u"Students"


class CustomUserAdmin(UserAdmin):
    exclude = ("students", )
    inlines = (
       StudentInline,
    )


@register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@register(TeacherStudent)
class TeacherStudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, CustomUserAdmin)