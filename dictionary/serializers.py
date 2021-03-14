from rest_framework import serializers
from .models import *

class WordPortugueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPortuguese
        fields = ['wordPortuguese']

class PronunciationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PronunciationType
        fields = ['pronunciationType']

class PhrasePortugueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhrasePortuguese
        fields = ['phrasePortuguese']

class WordKokamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordKokama
        fields = ['wordKokama']

class PhraseKokamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhraseKokama
        fields = ['phraseKokama']

class traduzSerializer(serializers.ModelSerializer):
    class Meta:
        model = traduz
        fields = ['portuguese', 'kokama']