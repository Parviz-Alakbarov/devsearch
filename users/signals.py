from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        send_mail(
            subject='Welcome to DevSearch',
            message='WE are glad you are here!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[profile.email],
            fail_silently=False,
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = instance.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
