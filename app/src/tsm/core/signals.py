from django.contrib.auth.models import Permission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import User


@receiver(pre_save, sender=User)
def update_user_to_staff(sender, instance, *args, **kwargs):
    instance.is_staff = True


@receiver(post_save, sender=User)
def add_permission_for_setting_star_students(sender, instance, *args, **kwargs):
    if not instance.is_superuser:
        teacher_student_permissions = Permission.objects.filter(
            content_type__app_label= 'core',
            content_type__model='teacherstudent',
            codename__in=['view_teacherstudent', 'change_teacherstudent'],
        )
        for permission in teacher_student_permissions:
            instance.user_permissions.add(permission)
