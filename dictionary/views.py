from rest_framework import viewsets, mixins
from .serializers import WordKokamaSerializer, WordsSerializer, PhraseKokamaSerializer, WordListSerializer
from .models import WordKokama, WordPortuguese, PhraseKokama, PhrasePortuguese, Translate
from django.views.decorators.http import require_http_methods

class KokamaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordKokamaSerializer

class WordListViewSet(viewsets.ModelViewSet):
    queryset = WordKokama.objects.all()
    serializer_class = WordListSerializer

class PhrasesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PhraseKokama.objects.all()
    serializer_class = PhraseKokamaSerializer

@require_http_methods(["POST", "GET"])
def add_translate(request):
    print("socorro\n\n")
    
    id = None
    word_kokama = WordKokama.objects.none()
    # Edit
    if id:
        word_kokama = WordKokama.objects.get(id=id)
        word_kokama.word_kokama = word_kokama=request.POST.get('word_kokama')
        word_kokama.pronunciation_type = request.POST.get('pronunciation_choises')
    else:
        word_kokama, created = WordKokama.objects.get_or_create(
            word_kokama=request.POST.get('word_kokama'),
            pronunciation_type=request.POST.get('pronunciation_choises'),
        )

    word_kokama.save()

    word_portuguese_total_forms = request.POST.get('word-portuguese-TOTAL_FORMS')
    for i in range(0, word_portuguese_total_forms):
        word_portuguese, _ = WordPortuguese.objects.get_or_create(words_portuguese=request.POST.get('word-portuguese-{}-word_portuguese'.format(i)))
        word_portuguese.save()
        translation, _ = Translate.objects.get_or_create(
            word_kokama=word_kokama,
            word_portuguese=word_portuguese
        )
        translation.save()


    phrase_total_forms = request.POST.get('phrase-TOTAL_FORMS')
    for i in range(0, phrase_total_forms):
        phrase_portuguese, _ = PhrasePortuguese.objects.get_or_create(phrase_portuguese=request.POST.get('phrase-{}-phrase_portuguese'.format(i)))
        phrase_portuguese.save()

        phrase_kokama, _ = PhraseKokama.objects.get_or_create(
            phrase_kokama=request.POST.get('phrase-{}-phrase_kokama'.format(i)),
            word_kokama=word_kokama,
            phrase_portuguese=phrase_portuguese,
        )
        phrase_kokama.save()

    return HttpResponse()

    