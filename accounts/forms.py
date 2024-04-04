from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = None
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # bio = forms.Textarea(widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = None
    
   
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name',)