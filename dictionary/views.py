from rest_framework import viewsets, mixins
from .serializers import *
from .models import *

class WordPortugueseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordPortuguese.objects.all()
    serializer_class = WordPortugueseSerializer

class PronunciationTypeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PronunciationType.objects.all()
    serializer_class = PronunciationTypeSerializer

class PhrasePortugueseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PhrasePortuguese.objects.all()
    serializer_class = PhrasePortugueseSerializer

class WordKokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer

class PhraseKokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PhraseKokama.objects.all()
    serializer_class = PhraseKokamaSerializer
