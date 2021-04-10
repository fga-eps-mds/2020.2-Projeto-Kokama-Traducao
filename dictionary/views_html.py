from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from .models import WordKokama, WordPortuguese
from .models import PhrasePortuguese, PhraseKokama, PronunciationType, Translate
from .forms import NewWordForm, AddNewPortugueseForm, AddNewPhraseForm

@require_http_methods(["GET", "POST"])
def list_words(request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
                        
            word_kokama = WordKokama.objects.all().order_by('-id')
            listWords = []
            for word in word_kokama:
                translations = Translate.objects.filter(word_kokama=word)
                translate = ', '.join([translate.word_portuguese.word_portuguese for translate in translations])
                listWords.append({"word_kokama":word, "translations":translate})

            return render(request, 'words/word_list.html', {'words': listWords})
        else:
            return HttpResponse('<h1>Erro interno do servidor</h1>', status=500)
    else:
        return redirect('/')


@require_http_methods(["GET", "POST"])
def view_word(request, id):
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
def add_word(request):
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

                pronunciation = PronunciationType.objects.get(id=pronunciation_type)
                pronunciation.save()
                
                kokama = WordKokama(word_kokama=kokama_word, pronunciation_type=pronunciation)
                try:
                    kokama.save()
                except:
                    return render(request, 'words/word_add.html', {'form': form, 'uniqueError':"A palavra já existe"})

                portuguese = WordPortuguese(word_portuguese=portuguese_word)
                portuguese.save()


                phrase_pt = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
                phrase_pt.save()

                phrase_kk = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=kokama, phrase_portuguese=phrase_pt)
                phrase_kk.save()

                translate = Translate(word_kokama=kokama, word_portuguese=portuguese)
                translate.save()

                return redirect('/traducao/adicionar_palavra/')
            else:
                return render(request, 'words/word_add.html', {'form': form})
    else:
        return redirect('/')


words_edit_url = 'words/word_edit.html'
words_list_url = '/traducao/lista_de_palavras/'

@require_http_methods(["GET", "POST"])
def edit_portuguese(request, id, field):

    if(request.method == 'GET'):
        form = AddNewPortugueseForm()
        return render(request, words_edit_url, {'form': form})
    else:
        form = AddNewPortugueseForm(request.POST)
        if form.is_valid():
            portuguese_word = request.POST.get('portuguese_word')
            wordPortuguese = WordPortuguese(word_portuguese=portuguese_word)
            wordPortuguese.save()

            word_kokama = get_object_or_404(WordKokama, pk=id)

            translate = Translate(word_kokama=word_kokama,
                                  word_portuguese=wordPortuguese)
            translate.save()

            return redirect(words_list_url + str(id))
        else:
            return render(request, words_edit_url, {'form': form})


def edit_phrases(request, id, field):
    if(request.method == 'GET'):

        form = AddNewPhraseForm()
        return render(request, words_edit_url, {'form': form})
    else:
        form = AddNewPhraseForm(request.POST)
        if form.is_valid():
            phrase_portuguese = request.POST.get('phrase_portuguese')
            phrase_kokama = request.POST.get('phrase_kokama')

            word_kokama = get_object_or_404(WordKokama, pk=id)

            phrase_pt = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
            phrase_pt.save()
            phrase_kk = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=word_kokama, phrase_portuguese=phrase_pt)
            phrase_kk.save()

            return redirect(words_list_url + str(id))
        else:
            return render(request, words_edit_url, {'form': form})


@require_http_methods(["GET", "POST"])
def edit_word(request, id, field):
    if(request.user.is_superuser):
        if field == "portugues":
            return edit_portuguese(request, id, field)
        elif field == "frases":
            return edit_phrases(request, id, field)
        else:
            return redirect(words_list_url + str(id))     
    else:
        return redirect('/')

@require_http_methods(["GET"])
def del_word(request, id):
    if(request.method == 'GET'):
        emp = WordKokama.objects.get(pk = id)
        emp.delete()
        return redirect('/traducao/lista_de_palavras/')

    return HttpResponse('Erro ao deletar', status=500)

@require_http_methods(["GET", "POST"])
def update_word(request, id):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            kokama = get_object_or_404(WordKokama, pk=id)
            translations = Translate.objects.filter(word_kokama=kokama)
            phrases = PhraseKokama.objects.filter(word_kokama=kokama)

            form = NewWordForm(
                initial={'kokama_word': kokama, 
                'portuguese_word':translations[0].word_portuguese,
                'phrase_kokama': phrases[0].phrase_kokama,
                'phrase_portuguese': phrases[0].phrase_portuguese,
                })
            return render(request, 'words/word_add.html', {'form': form})

        else:
            form = NewWordForm(request.POST)
            if form.is_valid():
                if(request.method == 'POST'):
                    emp = WordKokama.objects.get(pk = id)
                    emp.delete()
       
                portuguese_word = request.POST.get('portuguese_word')
                kokama_word = request.POST.get('kokama_word')
                pronunciation_type = request.POST.get('type_pronunciation')
                phrase_portuguese = request.POST.get('phrase_portuguese')
                phrase_kokama = request.POST.get('phrase_kokama')

                pronunciation = PronunciationType.objects.get(id=pronunciation_type)
                pronunciation.save()
                
                kokama = WordKokama(word_kokama=kokama_word, pronunciation_type=pronunciation)
                try:
                    kokama.save()
                except:
                    return redirect('/traducao/adicionar_palavra/')
                    
                portuguese = WordPortuguese(word_portuguese=portuguese_word)
                portuguese.save()


                phrase_pt = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
                phrase_pt.save()

                phrase_kk = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=kokama, phrase_portuguese=phrase_pt)
                phrase_kk.save()

                translate = Translate(word_kokama=kokama, word_portuguese=portuguese)
                translate.save()

    return redirect('/')
