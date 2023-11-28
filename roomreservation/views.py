from django.shortcuts import render
from .models import Room, Reservation
from .forms import ReservationForm
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
    args['page'] = 'home'
    
    return render(request, 'roomreservation/userhome.html', args)


def homeSignedOut(request):
    return render(request, 'roomreservation/home.html')

@login_required(login_url='/login')
def list_rooms(request):
    rooms = Room.objects.all().filter(deleted=False)
    return render(request, 'roomreservation/rooms.html',
                {
                    'rooms': rooms,
                })

@login_required(login_url='/login')
def reserve_room(request, room_id = None):
    args = {}
    args['page'] = 'reserveroom'
    args['account'] = Account.objects.get(user=request.user)    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.account = args['account']
            reservation.save()
            return HttpResponse('Reservation saved.')
        else:
            args['form'] = form
            print(form.errors)
            return render(request, 'roomreservation/reserveraroom.html', args)

    else:
        form = ReservationForm()
        args['form'] = form
        if room_id:
            form.fields['room'].initial = room_id
        return render(request, 'roomreservation/reserveraroom.html', args)