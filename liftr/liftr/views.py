from django.shortcuts import render

def home(request):
    return render(request, "base.html", {})


def coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print(latitude, longitude)
        return render(request, "base.html", {})
