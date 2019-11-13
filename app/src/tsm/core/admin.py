from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import User, Student, TeacherStudent


class TeacherFilter(admin.SimpleListFilter):
    title = 'Role'
    parameter_name = 'teacher'

    def lookups(self, request, model_admin):
        return (
            (1, 'Teacher'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '1':
            queryset = queryset.filter(is_superuser=False)
        return queryset


class StarFilter(admin.SimpleListFilter):
    title = 'Starred Students'
    parameter_name = 'is_star'

    def lookups(self, request, model_admin):
        return (
            (1, 'Starred Students'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '1':
            queryset = queryset.filter(is_star=True)
        return queryset


class StudentInline(admin.TabularInline):

    model = User.students.through
    verbose_name = u"Student"
    verbose_name_plural = u"Students"


class CustomUserAdmin(UserAdmin):
    exclude = ("students", )
    inlines = (
       StudentInline,
    )
    list_filter = (TeacherFilter,)


@register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@register(TeacherStudent)
class TeacherStudentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'is_star',)
    list_editable = ('is_star',)
    list_filter = (StarFilter,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(teacher=request.user)
        return qs

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['teacher', 'student']


admin.site.register(User, CustomUserAdmin)