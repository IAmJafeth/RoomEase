# Generated by Django 4.2.6 on 2023-11-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomreservation', '0005_reservation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_title',
            field=models.CharField(default='Reservation', max_length=30),
        ),
    ]
