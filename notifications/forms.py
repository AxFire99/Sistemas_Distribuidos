# notifications/forms.py
from django import forms
from django.contrib.auth.models import User  # Import the User model

class UserSelectForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Choose your option", to_field_name='username')
