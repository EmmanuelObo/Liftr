from django.shortcuts import render
from .pool import main

def load_user_pool(request):
    preference = Preference.objects.get()
    main.filter(request.user,)
    return render(request,"workout_buddy.html",{})