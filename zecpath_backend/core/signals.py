from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Candidate, Employer


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.CANDIDATE:
            Candidate.objects.create(
                user=instance,
                phone=instance.phone
            )

        elif instance.role == User.Role.EMPLOYER:
            Employer.objects.create(
                user=instance
            )