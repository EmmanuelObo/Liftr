from django.db import models
from django.contrib.auth.models import User

gender =(
('M','Male'),
( 'F', 'Female')
)

class Person(models.Model):
    user = models.OnetoOneField(User, on_delete=models.CASCADE())
    gender = models.CharField(choices=gender)
    age = models.IntegerField()
    location = models.CharField()
    bio = models.TextField()