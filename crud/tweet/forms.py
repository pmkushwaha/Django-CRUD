from django import forms
from .models import Tweet

class tweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']  #fields should be same as the given in the model
        
