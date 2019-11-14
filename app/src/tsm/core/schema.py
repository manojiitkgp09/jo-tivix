import graphene
from graphene_django.types import DjangoObjectType

from .models import User, Student, TeacherStudent


class UserType(DjangoObjectType):
    class Meta:
        model = User


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class TeacherStudentType(DjangoObjectType):
    class Meta:
        model = TeacherStudent


class CoreQuery:
    teachers = graphene.List(UserType)
    students = graphene.List(StudentType)

    def resolve_teachers(self, info, **kwargs):
        return User.objects.filter(is_superuser=False)

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()


class Query(CoreQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
