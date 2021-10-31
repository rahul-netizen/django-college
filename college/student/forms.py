from django import forms
from .models import Student


class StudentLoginForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Email'}))
    roll = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Roll Number'}))

    class Meta:
        model = Student
        fields = [
            'email',
            'roll',
            'course',
        ]
