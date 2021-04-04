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
            translations = Translate.objects.all().order_by('-id')
            # Need to remove duplicates translations.word_kokama from translations list
            return render(request, 'words/word_list.html', {'words': translations})
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

                portuguese = WordPortuguese(word_portuguese=portuguese_word)
                portuguese.save()

                pronunciation = PronunciationType.objects.get(id=pronunciation_type)
                pronunciation.save()

                phrase_PT = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
                phrase_PT.save()

                kokama = WordKokama(word_kokama=kokama_word, pronunciation_type=pronunciation)
                kokama.save()

                phrase_KK = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=kokama, phrase_portuguese=phrase_PT)
                phrase_KK.save()

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

            phrase_PT = PhrasePortuguese(phrase_portuguese=phrase_portuguese)
            phrase_PT.save()
            phrase_KK = PhraseKokama(phrase_kokama=phrase_kokama, word_kokama=word_kokama, phrase_portuguese=phrase_PT)
            phrase_KK.save()

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
