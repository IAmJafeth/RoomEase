# Generated by Django 4.2.6 on 2023-10-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomreservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(blank=True, default='room_pics/default.jpg', null=True, upload_to='room_pics'),
        ),
    ]