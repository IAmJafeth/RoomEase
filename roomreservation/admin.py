from django.contrib import admin
from .models import Room, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'description', 'status', 'deleted')
    list_filter = ('status', 'deleted')
    search_fields = ('id', 'name', 'description')
    ordering = ['name']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'account', 'title', 'date', 'start_time', 'end_time', 'status', 'created_at', 'deleted')
    list_filter = ('status', 'deleted')
    search_fields = ('id', 'title', 'description')
    ordering = ['date']

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)