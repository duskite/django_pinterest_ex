from django.forms import ModelForm, FileInput
from django import forms

from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname','message']

