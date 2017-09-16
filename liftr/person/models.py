from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

gender = (
    ('M','Male'),
    ( 'F', 'Female')
)

focus = (
    ('Weight Lifting', 'Weight Lifting'),
    ('Power Lifting','Power Lifting'),
    ('Cardio','Cardio'),
    ('HIIT','HIIT'),
    ('Plyometrics','Plyometrics'),
    ('Mixed', 'Mixed')
)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=gender, max_length=10, null=True)
    age = models.IntegerField(null=True)
    focus = models.CharField(choices=focus, max_length=15, null=True)
    location = models.CharField(max_length=30, null=True)
    bio = models.TextField(null=True)


    @receiver(post_save, sender=User)
    def register(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_changes(sender, instance, **kwargs):
        instance.person.save()

    def __str__(self):
        return self.user.username