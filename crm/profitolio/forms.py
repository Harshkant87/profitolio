from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Register a User

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

# Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

# Add a record
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['company_name', 'stock_symbol', 'buy_price', 'quantity', 'sell_price', 'buy_date', 'sell_date']


# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['company_name', 'stock_symbol', 'buy_price', 'quantity', 'sell_price', 'buy_date', 'sell_date']