from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from .models import WordKokama, WordPortuguese
from .models import PhrasePortuguese, PhraseKokama, PronunciationType,Translate
from .forms import NewWordForm, AddNewPortugueseForm, AddNewPhraseForm

@require_http_methods(["GET", "POST"])
def listWords(request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            translations = Translate.objects.all().order_by('-id')
            # Need to remove duplicates translations.word_kokama from translations list
            return render(request, 'words/word_list.html', {'words': translations})
        else:
            return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)
    else:
        return redirect('/')

def viewWord(request, id):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            kokama = get_object_or_404(WordKokama, pk=id)
            translations = Translate.objects.filter(word_kokama=kokama)
            phrases = PhraseKokama.objects.filter(word_kokama=kokama)

            context = {
                'kokama': kokama,
                'translations': translations,
                'phrases': phrases,
            }

            return render(request, 'words/word_view.html', context)
        else:
            return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)
    else:
        return redirect('/')



@require_http_methods(["GET", "POST"])
def addWord(request):
    
    if(request.user.is_superuser):
        
        if(request.method == 'GET'):
            form = NewWordForm()
            return render(request, 'words/word_add.html', {'form': form})
        
        else:
            form = NewWordForm(request.POST)

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
                return render(request, 'words/word_add.html', {'form': form})
    else:
        return redirect('/')


def editWord(request, id, field):
    if(request.user.is_superuser):

        if field == "portugues":
            if(request.method == 'GET'):
                form = AddNewPortugueseForm()
                return render(request, 'words/word_edit.html', {'form': form})
            else:
                form = AddNewPortugueseForm(request.POST)
                if form.is_valid():
                    portuguese_word = request.POST.get('portuguese_word')
                    wordPortuguese = WordPortuguese(word_portuguese=portuguese_word)
                    wordPortuguese.save()
                    
                    wordKokama = get_object_or_404(WordKokama, pk=id)

                    translate = Translate(word_kokama=wordKokama, word_portuguese=wordPortuguese)
                    translate.save()

                    return redirect('/traducao/lista_de_palavras/' + str(id))
                else:
                    return render(request, 'words/word_edit.html', {'form': form})

        elif field == "frases":
            if(request.method == 'GET'):
                
                form = AddNewPhraseForm()
                return render(request, 'words/word_edit.html', {'form': form})
            else:
                form = AddNewPhraseForm(request.POST)
                if form.is_valid():
                    phrase_portuguese = request.POST.get('phrase_portuguese')
                    phrase_kokama = request.POST.get('phrase_kokama')

                    wordKokama = get_object_or_404(WordKokama, pk=id)

                    phrasePortuguese = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
                    phrasePortuguese.save()
                    phraseKokama = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=wordKokama, phrase_portuguese=phrasePortuguese)
                    phraseKokama.save()

                    return redirect('/traducao/lista_de_palavras/' + str(id))
                else:
                    return render(request, 'words/word_edit.html', {'form': form})

        else:
            return redirect('/traducao/lista_de_palavras/' + str(id))
    else:
        return redirect('/')