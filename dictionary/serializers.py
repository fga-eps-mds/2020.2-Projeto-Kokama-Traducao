from rest_framework import serializers
from .models import *

class WordPortugueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPortuguese
        fields = ['portuguese_word']

class PronunciationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PronunciationType
        fields = ['pronunciation_type']

class PhrasePortugueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhrasePortuguese
        fields = ['portuguese_phrase']

class WordKokamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordKokama
        fields = ['kokama_word', 'pronunciation_type']

class PhraseKokamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhraseKokama
        fields = ['kokama_phrase', 'portuguese_phrase']

class traduzSerializer(serializers.ModelSerializer):
    class Meta:
        model = traduz
        fields = ['portuguese', 'kokama']