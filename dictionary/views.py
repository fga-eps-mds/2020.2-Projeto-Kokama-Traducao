from rest_framework import viewsets, mixins
from .serializers import WordKokamaSerializer
from .models import WordKokama


class KokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer
