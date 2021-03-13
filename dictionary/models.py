from django.db import models

class WordPortuguese(models.Model):
    wordPortuguese = models.CharField(max_length= 50)

    def __str__(self):
        return self.wordPortuguese
    
class PronunciationType(models.Model):
    pronunciationType = models.CharField(max_length=50)

    def __str__(self):
        return self.pronunciationType

class PhrasePortuguese(models.Model):
    phrasePortuguese = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.phrasePortuguese


class WordKokama(models.Model):
    wordKokama = models.CharField(max_length=50)
    pronunciationType = models.ForeignKey(
        PronunciationType,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.wordKokama

class PhraseKokama(models.Model):
    phraseKokama = models.TextField(null=False, blank=False)

    phrasePortuguese = models.ForeignKey(
        PhrasePortuguese, 
        on_delete= models.DO_NOTHING
    )

    wordKokama = models.ForeignKey(
        WordKokama,
        on_delete= models.DO_NOTHING
    )

    def __str__(self):
        return self.phraseKokama


class traduz(models.Model):
    portuguese = models.ForeignKey(
        WordPortuguese,
        on_delete= models.DO_NOTHING
    )

    kokama = models.ForeignKey(
        WordKokama,
        on_delete= models.DO_NOTHING
    )



