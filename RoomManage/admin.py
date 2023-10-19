from django.contrib import admin
from .models import Room, Reservation
# Register your models here.

# set up the admin site
admin.site.site_header = "Room Reservation System"
admin.site.site_title = "Room Reservation System"
admin.site.index_title = "Room Reservation System"

# show customer information on the admin dashboard
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'room_capacity', 'room_description', 'room_status')
    list_filter = ('room_status',)
    search_fields = ('room_id', 'room_name')
    ordering = ['room_id']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'room_id', 'user_id', 'reservation_date', 'reservation_start_time', 'reservation_end_time', 'reservation_description', 'reservation_status')
    list_filter = ('reservation_status',)
    search_fields = ('reservation_id', 'room_id', 'user_id')
    ordering = ['reservation_id']

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)



