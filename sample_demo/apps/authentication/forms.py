from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password": PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password": PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "first_name": TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": TextInput(attrs={"class": "form-control", "placeholder": "Last Name"})
        }