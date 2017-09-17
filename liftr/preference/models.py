from django.db import models

from person.models import Person


class Preference(models.Model):
    availability = []
    distance = models.IntegerField()
    user = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)


    def set_availability(self, days):
        self.availability = days

    def __str__(self):
        return "{}'s Preference".format(self.user.user.username)