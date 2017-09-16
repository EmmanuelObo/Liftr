from django.contrib import admin
from person.models import Person
from preference.models import Preference


# Register your models here.
admin.site.register(Person)
admin.site.register(Preference)