from django.apps import AppConfig


class RoomreservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'roomreservation'

    # def ready(self):
    #     import roomreservation.management.commands.updaterr
    #     roomreservation.management.commands.updaterr.Command().handle()
