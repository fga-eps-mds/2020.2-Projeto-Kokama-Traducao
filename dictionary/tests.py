from django.test import TestCase
from dictionary.models import WordPortuguese, PronunciationType, PhrasePortuguese


PORTUGUESE_WORD = 'portuguese word'
PRONUNCIATION_TYPE = 'both'
PORTUGUESE_PHRASE = 'portuguese phrase'

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
