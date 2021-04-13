from django.db import models

class WordPortuguese(models.Model):
    word_portuguese = models.CharField(max_length=50)

    def __str__(self):
        return self.word_portuguese

class PronunciationType(models.Model):
    pronunciation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.pronunciation_type


class PhrasePortuguese(models.Model):
    phrase_portuguese = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.phrase_portuguese


class WordKokama(models.Model):
    word_kokama = models.CharField(max_length=50)
    pronunciation_type = models.ForeignKey(
        PronunciationType,
        on_delete=models.DO_NOTHING,
        db_constraint=False
    )
    translations = models.ManyToManyField(
        WordPortuguese,
        through='Translate',
        through_fields=('word_kokama', 'word_portuguese'),
    )

    def __str__(self):
        return self.word_kokama


class PhraseKokama(models.Model):
    phrase_kokama = models.TextField(null=False, blank=False)
    word_kokama = models.ForeignKey(
        WordKokama,
        related_name='phrases',
        on_delete= models.DO_NOTHING,
        db_constraint=False
    )
    phrase_portuguese = models.ForeignKey(
        PhrasePortuguese, 
        on_delete= models.DO_NOTHING,
        db_constraint=False
    )

    def __str__(self):
        return self.phrase_kokama



class Translate(models.Model):
    word_kokama = models.ForeignKey(
        WordKokama,
        on_delete= models.CASCADE,
    )
    word_portuguese = models.ForeignKey(
        WordPortuguese,
        on_delete= models.CASCADE,
    )

    def __str__(self):
        return '%s <-> %s' % (self.word_kokama, self.word_portuguese)
