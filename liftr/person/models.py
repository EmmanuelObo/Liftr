from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from friendship.models import Friend

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
    longitude = models.DecimalField(max_digits=100, decimal_places=100, null=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=100, null=True)
    profile_pic = models.ImageField(null=True)

    @receiver(post_save, sender=User)
    def register(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_changes(sender, instance, **kwargs):
        instance.person.save()

    @property
    def friends(self):
        '''
        List of User's friends
        :return:
        '''
        return Friend.objects.friends(self.user)

    @property
    def reject_list(self):
        '''
        List of rejected friend requests
        '''
        return Friend.objects.rejected_requests(user=self.user)

    @property
    def pending_list(self):
        '''
        List of sent friend requests
        '''
        return Friend.objects.sent_requests(user=self.user)

    @property
    def awaiting_list(self):
        '''
        List of friend requests awaiting a response
        '''
        return Friend.objects.unread_request_count(user=self.user)

    def __str__(self):
        return self.user.username