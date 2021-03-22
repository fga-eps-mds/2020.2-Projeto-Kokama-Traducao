from django.http import HttpResponse
from django.shortcuts import render
from .models import WordKokama, WordPortuguese
from .models import PhrasePortuguese, PhraseKokama, PronunciationType,Translate

def add_translate(request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            return render(request, 'add_translation.html')
        elif(request.method == 'POST'):
            portuguese_word = request.POST.get('portuguese_word')
            kokama_word = request.POST.get('kokama_word')
            pronunciation_type = request.POST.get('type_pronunciation')
            phrase_portuguese = request.POST.get('phrase_portuguese')
            phrase_kokama = request.POST.get('phrase_kokama')
            # translate = request.POST.get('translate')
            
            wordPortuguese = WordPortuguese(word_portuguese=portuguese_word)
            wordPortuguese.save()
        
            pronunciationType = PronunciationType.objects.get(id=pronunciation_type)

            phrasePortuguese = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
            phrasePortuguese.save()
            
            wordKokama = WordKokama(word_kokama=kokama_word, pronunciation_type=pronunciationType)
            wordKokama.save()

            phraseKokama = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=wordKokama, phrase_portuguese=phrasePortuguese)
            phraseKokama.save()

            translate = Translate(word_kokama=wordKokama, word_portuguese=wordPortuguese)
            translate.save()

            return render(request, 'okay_translation.html')
    else:
        return HttpResponse('APENAS ADMINISTRADORES')