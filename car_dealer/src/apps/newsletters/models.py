from django.db import models
from django.conf import settings


class NewsLetter(models.Model):
    news_letter_id = models.IntegerField(primary_key=True, verbose_name="ID")
    email = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'

    def __str__(self):
        return self.email
