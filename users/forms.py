# Code derived from "Python Django Tutorial: Full-Featured Web App Part 6 - User Registration" Timestamp 33:35
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile" Timestamp 2:26
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Code Derived from "Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile" Timestamp 1:11
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
     model = Profile
     fields = ['image']




