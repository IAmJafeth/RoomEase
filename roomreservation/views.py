from django.shortcuts import render
from .models import Room, Reservation

# Create your views here.

def index(request):
    return render(request, 'roomreservation/home.html',
                {
                    'page' : 'home',
                })

def list_rooms(request):
    rooms = Room.objects.all().filter(active=True)
    return render(request, 'roomreservation/rooms.html',
                {
                    'page' : 'rooms',
                    'rooms': rooms,
                })



