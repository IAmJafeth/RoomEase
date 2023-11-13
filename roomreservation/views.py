from django.shortcuts import render
from .models import Room, Reservation
from account.models import Account
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import get_busy_rooms, get_free_rooms, next_reservation, all_next_reservations_account, current_reservations_account


# Create your views here.

def baseHome(request):
    if request.user.is_authenticated:
        return homeSignedIn(request)
    
    return homeSignedOut(request)

@login_required(login_url='/login')
def homeSignedIn(request):
    args = {}
    
    args['account'] = Account.objects.get(user=request.user)
    args['current_reservations_account'] = current_reservations_account(args['account'])
    args['next_reservations_account'] = all_next_reservations_account(args['account'])
    args['free_rooms'] = get_free_rooms()
    args['busy_rooms'] = get_busy_rooms()
    args['next_reservation_room'] = [next_reservation(room) for room in args['free_rooms']]
    
    return render(request, 'roomreservation/userhome.html', args)


def homeSignedOut(request):
    return render(request, 'roomreservation/home.html')

def list_rooms(request):
    rooms = Room.objects.all().filter(active=True)
    return render(request, 'roomreservation/rooms.html',
                {
                    'rooms': rooms,
                })



