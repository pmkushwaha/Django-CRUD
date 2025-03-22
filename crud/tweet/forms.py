from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

class tweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']  #fields should be same as the given in the model
        
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField
    class Meta:
        model=User
        fields=('username','email','password1','password2')