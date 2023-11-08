from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseHome, name='home'),
    path('rooms/', views.list_rooms, name='list_rooms'),
]





#