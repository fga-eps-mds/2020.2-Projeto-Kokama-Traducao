from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import PhrasePortuguese, PhraseKokama

class AddNewPhrase(forms.Form):
    phrase_portuguese = forms.RegexField(regex = '[\w ]*(<\w+>)[\w ]*')
    phrase_kokama = forms.RegexField(regex = '[\w ]*(<\w+>)[\w ]*')
