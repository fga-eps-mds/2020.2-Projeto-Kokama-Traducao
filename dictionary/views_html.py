from django.http import HttpResponse
from django.shortcuts import render
from .models import WordKokama, WordPortuguese
from .models import PhrasePortuguese, PhraseKokama


def add_translate(request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            return render(request, 'add_translation.html')
        elif(request.method == 'POST'):
            portuguese_word = request.POST.get('portuguese_word')
            kokama_word = request.POST.get('kokama_word')
            phrase_portuguese = request.POST.get('phrase_portuguese')
            phrase_kokama = request.POST.get('phrase_kokama')

            wordPortuguese = WordPortuguese(word_portuguese=portuguese_word)
            wordPortuguese.save()
            
            wordKokama = WordKokama(word_kokama=kokama_word)
            wordKokama.save()
            
            phrasePortuguese = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
            phrasePortuguese.save()
            
            phraseKokama = PhraseKokama(phrase_kokama=portuguese_word)
            phraseKokama.save()

            return HttpResponse('Okay')
    else:
        return HttpResponse('APENAS ADMINISTRADORES')