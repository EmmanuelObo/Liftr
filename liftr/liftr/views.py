from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from preference.models import Preference
from person.pool import main
from person.friendships import main as friends
from random import randint


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/workout')
    return render(request, "sub_templates/home.html", {})

def workout(request):
    if request.method == 'POST':
        pk = request.POST.get('send_request').replace("/","")
        print("Value of pk: {} ".format(pk.replace("/","")))
        recipient = User.objects.get(username=str(pk))
        friends.send_request(request.user,recipient)
        request.user.save()
        preference = Preference.objects.get(user=request.user.person)
        users = User.objects.all()
        user_pool = main.filter(request.user.person, preference, users)
        return render(request, "sub_templates/workout_buddy.html", {"first_user": user_pool[1]})

    else:
        preference = Preference.objects.get(user=request.user.person)
        users = User.objects.all()
        user_pool = main.filter(request.user.person,preference, users)
        print(user_pool)
        return render(request, "sub_templates/workout_buddy.html", {"first_user": user_pool[0]})

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            x = login(request, user)
            print(x)
            return HttpResponseRedirect('/workout')
        else:
            response = 'Login Unsuccessful'
            return render(request, 'sub_templates/login.html', {'response': response})
    else:
        return render(request, 'sub_templates/login.html')

def edit(request):
    return render(request, 'sub_templates/edit.html')

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/home')

def coordinates(request):
    if request.method == 'GET':
        request.user.person.latitude = randint(30,50)
        request.user.person.longitude = randint(-110, -70)
        geolocator = Nominatim()
        current_location = ("{}, {}".format(request.user.person.latitude, request.user.person.longitude))
        location = geolocator.reverse(current_location)
        print(location.address)
        return render(request, "sub_templates/edit.html", {'data' : location.address})
    else:
        return render(request,  "sub_templates/workout.html")
