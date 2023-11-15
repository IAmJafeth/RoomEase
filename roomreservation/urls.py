from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseHome, name='home'),
    path('rooms/', views.list_rooms, name='list_rooms'),
    path('reserve/', views.reserve_room, name='reserve_room'),
    path('reserve/<int:room_id>/', views.reserve_room, name='reserve_room'),
]





#