from django.core.management.base import BaseCommand, CommandError
from roomreservation.models import Room, Reservation
from roomreservation.utils import get_ongoing_reservations
from django.utils import timezone

class Command(BaseCommand):
    help = 'Sets the status of rooms and reservations'

    def handle(self, *args, **options):
        rooms = Room.objects.all().filter(active=True)
        reservations = get_ongoing_reservations()
        for room in rooms:
            if room in reservations:
                room.status = False
                print('Room: ', room.name, ' is busy')
            else:
                room.status = True
                print('Room: ', room.name, ' is free')
            room.save()
        print('Rooms status updated')
        reservations = Reservation.objects.all()

        for reservation in reservations:
            if reservation.date < timezone.now().date():
                reservation.status = False
                print('Reservation: ', reservation.title, ' is in the past')
            elif reservation.date == timezone.now().date():
                if reservation.end_time < timezone.now().time():
                    reservation.status = False
                    print('Reservation: ', reservation.title, ' is in the past')
            reservation.save()
        print('Reservations status updated')