from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from configapp.models import Sms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Majburiy va to`g`ri email kiriting')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SmsForm(forms.ModelForm):
    class Meta:
        model = Sms
        fields = "__all__"