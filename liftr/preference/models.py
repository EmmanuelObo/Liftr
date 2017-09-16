from django.db import models

from person.models import Person


class Preference(models.Model):
    availability = []
    distance = models.IntegerField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


    def set_availability(self, days):
        self.availability = days



