from rest_framework import viewsets, mixins
from .serializers import WordKokamaSerializer, WordsSerializer
from .models import WordKokama


class KokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer

class WordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordsSerializer