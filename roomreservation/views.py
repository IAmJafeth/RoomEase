from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'roomreservation/home.html')

def list_rooms(request):
    return render(request, 'roomreservation/rooms.html')