from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import WordKokama, WordPortuguese
from .models import PhrasePortuguese, PhraseKokama, PronunciationType,Translate
from .forms import AddNewWord

@require_http_methods(["GET", "POST"])
def add_translate(request):
    
    if(request.user.is_superuser):
        
        if(request.method == 'GET'):
            form = AddNewWord()
            return render(request, 'add_translation.html', {'form': form})
        
        elif(request.method == 'POST'):
            form = AddNewWord(request.POST)

            if form.is_valid():

                portuguese_word = request.POST.get('portuguese_word')
                kokama_word = request.POST.get('kokama_word')
                pronunciation_type = request.POST.get('type_pronunciation')
                phrase_portuguese = request.POST.get('phrase_portuguese')
                phrase_kokama = request.POST.get('phrase_kokama')
                
                wordPortuguese = WordPortuguese(word_portuguese=portuguese_word)
                wordPortuguese.save()
                
                pronunciationType = PronunciationType.objects.get(id=pronunciation_type)
                pronunciationType.save()

                phrasePortuguese = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
                phrasePortuguese.save()
                
                wordKokama = WordKokama(word_kokama=kokama_word, pronunciation_type=pronunciationType)
                wordKokama.save()
    
                phraseKokama = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=wordKokama, phrase_portuguese=phrasePortuguese)
                phraseKokama.save()

                translate = Translate(word_kokama=wordKokama, word_portuguese=wordPortuguese)
                translate.save()

                return redirect('/traducao/adicionar_palavra/')
            else:
                return render(request, 'add_translation.html', {'form': form})
    else:
        return HttpResponse('<h1>Você não tem autorização para visualizar esta página</h1>',
                            status=401)

@require_http_methods(["GET", "POST"])
def list_translation (request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            word_kokama = WordKokama.objects.all()
            word_portuguese= WordPortuguese.objects.all()
            phrase_portuguese= PhrasePortuguese.objects.all()
            phrase_kokama= PhraseKokama.objects.all()
            words = zip(word_kokama, word_portuguese, phrase_portuguese,phrase_kokama)
            context = {
                'words': words,
            }
            print(context)
            return render(request, 'list_translation.html', context)
        else:
            return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)
    else:
        return HttpResponse('<h1>Você não tem autorização para visualizar esta página</h1>',
                            status=401)
