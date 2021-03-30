from django import forms
from django.core.validators import RegexValidator
from .models import Email

class AddEmail(forms.Form):
    
    email = forms.EmailField(
        label='e_mail', 
        error_messages={'required': ("Digite um email válido")},
    )
