from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.send_test, name='test'),
]





#