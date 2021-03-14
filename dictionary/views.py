from rest_framework import viewsets, mixins
from .serializers import *
from .models import *

class DictionaryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordPortuguese.objects.all()
    serializer_class = WordPortugueseSerializer
    filter_fields = ['code_pt']
