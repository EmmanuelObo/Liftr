from django.contrib.auth.models import User
from django.shortcuts import render

from liftr.preference.models import Preference
from .pool import main

def load_user_pool(request):
    preference = Preference.objects.get()
    users = User.objects.all()
    user_pool = main.filter(request.user,preference, users)
    return render(request,"workout_buddy.html",{"user_pool": user_pool})