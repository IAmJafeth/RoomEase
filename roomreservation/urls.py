from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rooms/', views.list_rooms, name='list_rooms'),
]





#