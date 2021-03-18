from django.contrib import admin
from .models import WordPortuguese, WordKokama, Translate
from .models import PhraseKokama, PhrasePortuguese, PronunciationType


admin.site.register(WordPortuguese)
admin.site.register(WordKokama)
admin.site.register(PhrasePortuguese)
admin.site.register(PhraseKokama)
admin.site.register(PronunciationType)
admin.site.register(Translate)
