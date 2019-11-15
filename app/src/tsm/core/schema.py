import graphene
from django_filters import FilterSet
from graphene_django.types import DjangoObjectType
from graphene_django_extras import (
    DjangoListObjectType,
    DjangoSerializerType,
    DjangoObjectType,
    DjangoListObjectField,
    LimitOffsetGraphqlPagination,
)


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
        description = "Type definition for all students of teacher"


class StarStudentFilter(FilterSet):
    class Meta:
        model = TeacherStudent
        fields = ['is_star']


class UserListType(DjangoListObjectType):
    class Meta:
        description = " Type definition for teachers list with their starred students "
        model = TeacherStudent
        pagination = LimitOffsetGraphqlPagination(
            default_limit=25,
        )  # ordering can be: string, tuple or list


class CoreQuery:
    teachers = graphene.List(UserType)
    students = graphene.List(StudentType)
    teacher_with_star_students = DjangoListObjectField(
        UserListType,
        filterset_class=StarStudentFilter,
        description='All Users query',
    )

    def resolve_teachers(self, info, **kwargs):
        return User.objects.filter(is_superuser=False)

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()


class Query(CoreQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
