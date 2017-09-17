from django.shortcuts import render
from geopy.geocoders import Nominatim

def home(request):
    return render(request, "base.html", {})


def coordinates(request):
    if request.method == 'POST':
        print("hello")
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print("latitude{} longitude{}".format(latitude,longitude))
        geolocator = Nominatim()

        location = geolocator.reverse("{}, {}".format(latitude,longitude))
        print(location.address)
        return render(request, "base.html", {})
