from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

from django.contrib.auth.models import User

def home(request):
    return render(request, "base.html", {})


def coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        current_user = User.objects.get(username='Test')
        other_user = User.objects.get(username='TEST2')
        geolocator = Nominatim()
        other_user.person.latitude = 38
        other_user.person.longitude = -77
        current_user.person.latitude = float(latitude)
        current_user.person.longitude = float(longitude)
        current_location = (current_user.person.latitude, current_user.person.longitude)
        other_location = (other_user.person.latitude, other_user.person.longitude)
        print(vincenty(current_location, other_location).miles)
        print(current_user.person.dict())
        print(other_user.person.dict())
        return render(request, "base.html", {})
