from .models import Room, Reservation
from django.utils import timezone

def get_ongoing_reservations():
    reservations = Reservation.objects.all().filter(active=True, status=True)

    current_reservations = []
    for reservation in reservations:
        if reservation.date == timezone.localdate():
            if reservation.start_time <= timezone.localtime().time() and reservation.end_time >= timezone.localtime().time():
                current_reservations.append(reservation)
    return current_reservations

def get_busy_rooms():
    current_reservations = get_ongoing_reservations()
    current_rooms = []
    for reservation in current_reservations:
        if not reservation.room in current_rooms:
            current_rooms.append(reservation.room)

    return current_rooms

def get_free_rooms():
    rooms = Room.objects.all().filter(active=True, status=True)
    free_rooms = []
    for room in rooms:  
        if not room in get_busy_rooms():
            free_rooms.append(room)
    return free_rooms

def next_reservation(room):
    reservations = Reservation.objects.all().filter(active=True, status=True, room=room).order_by('date', 'start_time')
    for reservation in reservations:
        if reservation.date > timezone.localdate():
            return reservation
        if reservation.date == timezone.localdate():
            if reservation.start_time > timezone.localtime().time():
                return reservation
    return None 
def all_next_reservations_account(account):
    reservations = Reservation.objects.all().filter(active=True, status=True, account=account).order_by('date', 'start_time')
    
    next_reservations = []
    for reservation in reservations:
        if reservation.date > timezone.localdate():
            next_reservations.append(reservation)
        if reservation.date == timezone.localdate():
            if reservation.start_time > timezone.localtime().time():
                
                next_reservations.append(reservation)

    return next_reservations

def current_reservations_account(account):
    reservations = Reservation.objects.all().filter(active=True, status=True, account=account).order_by('date', 'start_time')
    
    current_reservations = []
    for reservation in reservations:
        if reservation.date == timezone.localdate():
            if reservation.start_time <= timezone.localtime().time() and reservation.end_time >= timezone.localtime().time():
                current_reservations.append(reservation)
    return current_reservations
