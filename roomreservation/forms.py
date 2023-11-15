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

    def is_valid(self) -> bool:
        valid = super(ReservationForm, self).is_valid()
        if not valid:
            return valid

        if self.cleaned_data['start_time'] >= self.cleaned_data['end_time']:
            self.add_error('start_time', 'Start time must be before end time')
            return False

        return True