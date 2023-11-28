from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'date', 'start_time', 'end_time', 'title', 'description']
        widgets = {
            'room': forms.Select(attrs={'class':  'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def checkRoomAvailability(self, room, date, start_time, end_time):
        reservations = Reservation.objects.filter(room=room, date=date)
        for reservation in reservations:
            if reservation.start_time < start_time < reservation.end_time:
                return False
            if reservation.start_time < end_time < reservation.end_time:
                return False
        return True

    def is_valid(self) -> bool:
        valid = super(ReservationForm, self).is_valid()
        if not valid:
            return valid
        
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        room = self.cleaned_data['room']
        date = self.cleaned_data['date']


        if start_time >= end_time:
            self.add_error('start_time', 'Start time must be before end time')
            return False
        
        if not self.checkRoomAvailability(room, date, start_time, end_time):
            self.add_error('room', 'Room is not available at that time')
            return False

        return True