from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


OCCUPATION_CHOICES = [
    ('student', 'Student'),
    ('engineer', 'Engineer'),
    ('teacher', 'Teacher'),
    ('doctor', 'Doctor'),
    ('developer', 'Developer'),
    ('musician ', 'Musician')
]

EDUCATION_CHOICES = [
    ('high school', 'High School'),
    ('college', 'College'),
    ('graduate school', 'Graduate School'),
    ('no education', 'No Formal education')
]

INTERESTS_CHOICES = [
    ('music', 'Music'),
    ('sports', 'Sports'),
    ('technology', 'Technology'),
    ('coding', 'Coding')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    email = models.EmailField()
    profile_picture = ResizedImageField(size=[500, 300], upload_to='profile_pics', blank=True, null=True)
    occupation = models.CharField(max_length=255, choices=OCCUPATION_CHOICES, blank=True, null=True)
    education = models.CharField(max_length=255, choices=EDUCATION_CHOICES, blank=True, null=True)
    interests = models.CharField(max_length=255, choices=INTERESTS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a Profile when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)