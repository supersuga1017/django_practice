from django.db import models

# Create your models here.
class Diary(models.Model):

    title = models.CharField(verbose_name='タイトル',max_length=40)
    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title