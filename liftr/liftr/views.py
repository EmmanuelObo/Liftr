from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):
    return render(request, "sub_templates/home.html", {})

def login_screen(request):
    return render(request, "sub_templates/login.html", {})


def workout(request):
    return render(request, "sub_templates/workout_buddy.html", {})

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("username {} password {}".format(username,password))
    if request.user.is_authenticated():
        print(request.user)
        return HttpResponseRedirect('/workout')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home')

    else:
        response = 'Login Unsuccessful'
        return render(request, 'login.html', {'response': response})

    return render(request, 'login.html', {'form': form, 'response': response})


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
