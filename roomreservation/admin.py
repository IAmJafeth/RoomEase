from django.contrib import admin
from .models import Room, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'room_capacity', 'room_description', 'room_status', 'active')
    list_filter = ('room_status', 'active')
    search_fields = ('room_id', 'room_name', 'room_description')
    ordering = ['room_name']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'room', 'user', 'reservation_date', 'reservation_start_time', 'reservation_end_time', 'reservation_description', 'reservation_status', 'active')
    list_filter = ('reservation_status', 'active')
    search_fields = ('reservation_id', 'room', 'user', 'reservation_date', 'reservation_start_time', 'reservation_end_time', 'reservation_description')
    ordering = ['reservation_date']

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)