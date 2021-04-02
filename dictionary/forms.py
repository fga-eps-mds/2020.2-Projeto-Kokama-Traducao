from django import forms
from django.core.validators import RegexValidator
from .models import WordKokama, WordPortuguese, PhraseKokama, PhrasePortuguese

class PortugueseForm(forms.ModelForm):

    class Meta:
        model = WordPortuguese
        fields = ('word_portuguese',)

class KokamaForm(forms.ModelForm):

    class Meta:
        model = WordKokama
        fields = ('word_kokama',)

class PhrasePortuguese(forms.ModelForm):
    class Meta:
        model= PhrasePortuguese
        fields = ('phrase_portuguese',)


class PhraseKokama (forms.ModelForm):
    class Meta:
        model= PhraseKokama
        fields = ('phrase_kokama','word_kokama','phrase_portuguese')


PRONUNCIATION_CHOICES =(
    ("1", "Geral"),
    ("2", "Feminino"),
    ("3", "Masculino"),
)

class NewWordForm(forms.Form):

    kokama_word = forms.CharField(
        label='kokama_word',
        error_messages={'required': 'Preencha este campo.'}
    )

    portuguese_word = forms.CharField(
        label='portuguese_word',
        error_messages={'required': 'Preencha este campo.'}
    )
    
    type_pronunciation = forms.ChoiceField(
        choices = PRONUNCIATION_CHOICES,
        label='type_pronunciation',
    )

    phrase_kokama = forms.RegexField(
        label='phrase_kokama', 
        regex='.*<.+>.*',
        error_messages={'invalid': ("A frase deve conter uma palavra destacada com <>. Ex: <panara>.")},
    )
    
    phrase_portuguese = forms.RegexField(
        label='phrase_portuguese', 
        regex='.*<.+>.*',
        error_messages={'invalid': ("A frase deve conter uma palavra destacada com <>. Ex: <banana>.")},
    
    )

    
  