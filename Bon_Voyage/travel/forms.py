from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','dob','password1','password2')