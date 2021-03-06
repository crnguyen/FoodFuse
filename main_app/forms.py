from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SearchForm(forms.Form):
    location = forms.CharField( label='', max_length=300, widget=forms.TextInput(attrs={'style': 'height: 30px'}))
    
class RestaurantForm(forms.Form):
    restaurant = forms.CharField(label='Enter a restaurant', max_length=300, widget=forms.TextInput(attrs={'style': 'height: 30px'}))

class FavoriteForm(forms.Form):
    favorites = forms.CharField()
