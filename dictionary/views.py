from rest_framework import viewsets, mixins
from .serializers import WordKokamaSerializer, WordsSerializer, PhraseKokamaSerializer
from .models import WordKokama, PhraseKokama


class KokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer

# um pra frase e outro pra palavras
class WordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordsSerializer

class PhrasesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PhraseKokama.objects.all()
    serializer_class = PhraseKokamaSerializer