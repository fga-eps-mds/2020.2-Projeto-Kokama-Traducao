from django.test import TestCase, RequestFactory
from dictionary.models import WordPortuguese, PronunciationType, PhrasePortuguese, WordKokama, Translate, PhraseKokama
from django.apps import apps
from .apps import DictionaryConfig
from .views import add_translate, authenticate, delete_word_kokama, WordListViewSet
from decouple import config


PORTUGUESE_WORD = 'portuguese word'
PRONUNCIATION_TYPE = 'both'
PORTUGUESE_PHRASE = 'portuguese phrase'
KOKAMA_WORD = 'kokama word'
KOKAMA_PHRASE = 'kokama phrase'


class WordPortugueseModelTest(TestCase):
    def setUp(self):
        WordPortuguese.objects.create(word_portuguese=PORTUGUESE_WORD)
        
    def test_word_portuguese_str(self):
        portuguese_word = WordPortuguese.objects.get(word_portuguese=PORTUGUESE_WORD)
        self.assertEqual(str(portuguese_word), PORTUGUESE_WORD)

    def test_word_portuguese_length(self):
        portuguese_word_correct = WordPortuguese.objects.get(word_portuguese=PORTUGUESE_WORD)
        self.assertLessEqual(len(portuguese_word_correct.word_portuguese), 50)

        portuguese_word_wrong = WordPortuguese.objects.create(word_portuguese='word portuguese with more than max_length(fifty) characters in it')
        self.assertGreater(len(portuguese_word_wrong.word_portuguese), 50)


class PronunciationTypeModelTest(TestCase):
    def setUp(self):
        PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        
    def test_pronunciation_type_str(self):
        pronunciation = PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        self.assertEqual(str(pronunciation), PRONUNCIATION_TYPE)

    def test_pronunciation_type_length(self):
        pronunciation_correct = PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        self.assertLessEqual(len(pronunciation_correct.pronunciation_type), 50)

        pronunciation_wrong = PronunciationType.objects.create(pronunciation_type='pronunciation type with more than max_length(fifty) characters in it')
        self.assertGreater(len(pronunciation_wrong.pronunciation_type), 50)


class PhrasePortugueseModelTest(TestCase):
    def setUp(self):
        PhrasePortuguese.objects.create(phrase_portuguese=PORTUGUESE_PHRASE)
        
    def test_phrase_portuguese_str(self):
        portuguese_phrase = PhrasePortuguese.objects.get(phrase_portuguese=PORTUGUESE_PHRASE)
        self.assertEqual(str(portuguese_phrase), PORTUGUESE_PHRASE)


class WordKokamaModelTest(TestCase):
    def setUp(self):
        pronunciation = PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        WordKokama.objects.create(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=pronunciation
        )

    def test_word_kokama_str(self):
        kokama_word = WordKokama.objects.get(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        )
        self.assertEqual(str(kokama_word), KOKAMA_WORD)

    def test_word_kokama_length(self):
        kokama_word_correct = WordKokama.objects.get(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        )
        self.assertLessEqual(len(kokama_word_correct.word_kokama), 50)

        kokama_word_wrong = WordKokama.objects.create(
            word_kokama='kokama word with more than max_length(fifty) characters in it',
            pronunciation_type=PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        )
        self.assertGreater(len(kokama_word_wrong.word_kokama), 50)


class TranslateModelTest(TestCase):

    def setUp(self):
        kokama_word = WordKokama.objects.create(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        )
        portuguese_word = WordPortuguese.objects.create(word_portuguese=PORTUGUESE_WORD)
        Translate.objects.create(
            word_portuguese=portuguese_word,
            word_kokama=kokama_word,
        )
        
    def test_translate_str(self):
        kokama_word = WordKokama.objects.get(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        )
        portuguese_word = WordPortuguese.objects.get(word_portuguese=PORTUGUESE_WORD)
        translate = Translate.objects.get(
            word_portuguese=portuguese_word,
            word_kokama=kokama_word
        )
        
        self.assertEqual(str(translate), '%s <-> %s' % (KOKAMA_WORD, PORTUGUESE_WORD))


class PhraseKokamaModelTest(TestCase):
    def setUp(self):
        kokama_word = WordKokama.objects.create(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        )
        portuguese_phrase = PhrasePortuguese.objects.create(phrase_portuguese=PORTUGUESE_PHRASE)
        PhraseKokama.objects.create(
            phrase_kokama=KOKAMA_PHRASE,
            word_kokama=kokama_word,
            phrase_portuguese=portuguese_phrase,
        )
        
    def test_phrase_kokama_str(self):
        kokama_word = WordKokama.objects.get(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=PronunciationType.objects.get(pronunciation_type=PRONUNCIATION_TYPE)
        )
        portuguese_phrase = PhrasePortuguese.objects.get(phrase_portuguese=PORTUGUESE_PHRASE)
        kokama_phrase = PhraseKokama.objects.create(
            phrase_kokama=KOKAMA_PHRASE,
            word_kokama=kokama_word,
            phrase_portuguese=portuguese_phrase,
        )
        
        self.assertEqual(str(kokama_phrase), KOKAMA_PHRASE)


class DictionaryConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(DictionaryConfig.name, 'dictionary')
        self.assertEqual(apps.get_app_config('dictionary').name, 'dictionary')


# Views

class AuthenticateTest(TestCase):

    def test_authenticate(self):
        user_ip_correct = config('ALLOWED_IP_LIST')
        result = authenticate(user_ip_correct)
        self.assertTrue(result)

        user_ip_wrong = 'wrong_ip'
        result = authenticate(user_ip_wrong)
        self.assertFalse(result)


class DeleteWordKokama(TestCase):

    def setUp(self):
        # Create WordKokama
        pronunciation = PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        kokama_word = WordKokama.objects.create(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=pronunciation
        )
        # Create PhrasePortuguese
        portuguese_phrase = PhrasePortuguese.objects.create(phrase_portuguese=PORTUGUESE_PHRASE)
        # Create PhraseKokama
        PhraseKokama.objects.create(
            phrase_kokama=KOKAMA_PHRASE,
            word_kokama=kokama_word,
            phrase_portuguese=portuguese_phrase,
        )
        # Create WordPortuguese
        portuguese_word = WordPortuguese.objects.create(word_portuguese=PORTUGUESE_WORD)
        # Create Translate
        Translate.objects.create(
            word_portuguese=portuguese_word,
            word_kokama=kokama_word,
        )
        kokama_word.translations.add(portuguese_word)

    def test_delete_word_kokama(self):
        kokama_word = WordKokama.objects.get(word_kokama=KOKAMA_WORD)
        delete_word_kokama(kokama_word)
        self.assertFalse(WordKokama.objects.filter(word_kokama=str(kokama_word)).exists())


class WordListViewSetTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request_wrong = self.factory.delete('/1/')
        self.request_correct = self.factory.delete('/1/', REMOTE_ADDR=config('ALLOWED_IP_LIST'))

    def test_destroy(self):
        response = WordListViewSet.destroy(WordListViewSet, self.request_wrong)
        self.assertEqual(response.status_code, 403)

        response = WordListViewSet.destroy(WordListViewSet, self.request_correct)
        self.assertEqual(response.status_code, 500)


class AddTranslateTest(TestCase):

    def setUp(self):
        pronunciation = PronunciationType.objects.create(pronunciation_type=PRONUNCIATION_TYPE)
        kokama_word = WordKokama.objects.create(
            word_kokama=KOKAMA_WORD,
            pronunciation_type=pronunciation
        )

        context = [
            # Repeated
            {
                'pronunciation_choises': pronunciation.id,
                'word_kokama': kokama_word,
                'word-portuguese-TOTAL_FORMS': '1',
                'word-portuguese-0-word_portuguese': PORTUGUESE_WORD,
                'phrase-TOTAL_FORMS': '1',
                'phrase-0-phrase_portuguese': PORTUGUESE_PHRASE,
                'phrase-0-phrase_kokama': KOKAMA_PHRASE
            },
            {
                'pronunciation_choises': pronunciation.id,
                'word_kokama': {
                    'word_kokama': 'kokama word 2',
                    'pronunciation_type': pronunciation
                },
                'word-portuguese-TOTAL_FORMS': '1',
                'word-portuguese-0-word_portuguese': 'portuguese word 2',
                'phrase-TOTAL_FORMS': '1',
                'phrase-0-phrase_portuguese': 'portuguese phrase 2',
                'phrase-0-phrase_kokama': 'kokama phrase 2'
            }
        ]

        self.factory = RequestFactory()
        self.request_wrong = self.factory.post('/', context[0])
        self.request_correct_add_repeated = self.factory.post('/', context[0], REMOTE_ADDR=config('ALLOWED_IP_LIST'))
        self.request_correct_add = self.factory.post('/', context[1], REMOTE_ADDR=config('ALLOWED_IP_LIST'))
        self.request_correct_edit_repeated = self.factory.post('/', context[1], REMOTE_ADDR=config('ALLOWED_IP_LIST'))

    def test_add_translate(self):

        # Add
        response = add_translate(self.request_wrong, id=None)
        self.assertEqual(response.status_code, 403)

        response = add_translate(self.request_correct_add_repeated, id=None)
        self.assertEqual(response.status_code, 400)

        response = add_translate(self.request_correct_add, id=None)
        self.assertEqual(response.status_code, 200)

        # Edit
        response = add_translate(self.request_correct_edit_repeated, id=1)
        self.assertEqual(response.status_code, 400)
