from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {
            'username': '',
        }
class AdminFormRegister(UserCreationForm):
    secret_token = forms.CharField(
        label="Secret Token",
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']