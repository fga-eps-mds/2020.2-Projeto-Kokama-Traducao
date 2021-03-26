from django import forms
from django.core.validators import RegexValidator
from .models import PhrasePortuguese, PhraseKokama

PRONUNCIATION_CHOICES =(
    ("1", "Geral"),
    ("2", "Feminino"),
    ("3", "Masculino"),
)

class AddNewPhrase(forms.Form):
    
    phrase_portuguese = forms.RegexField(
        label='phrase_portuguese', 
        regex='.*<.+>.*',
        error_messages={'invalid': ("A frase deve conter uma palavra destacada com <>. Ex: <banana>.")},
    
    )

    phrase_kokama = forms.RegexField(
        label='phrase_kokama', 
        regex='.*<.+>.*',
        error_messages={'invalid': ("A frase deve conter uma palavra destacada com <>. Ex: <panara>.")},
    )

   
    word_portuguese = forms.CharField(
        label='word_portuguese',
        error_messages={'required': 'Preencha este campo.'}
    )
    
    word_kokama = forms.CharField(
        label='word_kokama',
        error_messages={'required': 'Preencha este campo.'}
    )
    
    type_pronunciation = forms.ChoiceField(
        choices = PRONUNCIATION_CHOICES,
        label='type_pronunciation',
    )


    