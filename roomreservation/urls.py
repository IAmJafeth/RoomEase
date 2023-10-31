from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.list_rooms, name='list_rooms'),
]





#