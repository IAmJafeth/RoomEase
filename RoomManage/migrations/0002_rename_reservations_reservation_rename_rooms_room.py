# Generated by Django 4.2.6 on 2023-10-17 03:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RoomManage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
