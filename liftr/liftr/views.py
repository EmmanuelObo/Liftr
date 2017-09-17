from django.shortcuts import render
from geopy.geocoders import Nominatim

def home(request):
    return render(request, "base.html", {})


def coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        geolocator = Nominatim()
        
        print(latitude, longitude)
        return render(request, "base.html", {})
