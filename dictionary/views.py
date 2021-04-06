from rest_framework import viewsets, mixins
from .serializers import WordKokamaSerializer, WordsSerializer
from .models import WordKokama


class KokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer

# um pra frase e outro pra palavras
class WordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordsSerializer