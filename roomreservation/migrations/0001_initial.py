# Generated by Django 4.2.7 on 2023-11-16 02:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('pic', models.ImageField(blank=True, default='room_pics/default.jpg', null=True, upload_to='room_pics')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 16, 2, 11, 12, 892773, tzinfo=datetime.timezone.utc))),
                ('status', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomreservation.room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
