from django.contrib import admin
from .models import Room, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'description', 'status', 'active')
    list_filter = ('status', 'active')
    search_fields = ('id', 'name', 'description')
    ordering = ['name']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'account', 'title', 'date', 'start_time', 'end_time', 'status', 'created_at', 'active')
    list_filter = ('status', 'active')
    search_fields = ('id', 'title', 'description')
    ordering = ['date']

    actions = ['make_inactive', 'make_active']

    def make_inactive(self, request, queryset):
        queryset.update(active=False)
    make_inactive.short_description = "Mark selected reservations as inactive"

    def make_active(self, request, queryset):
        queryset.update(active=True)
    make_active.short_description = "Mark selected reservations as active"





admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)