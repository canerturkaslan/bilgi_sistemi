from django.db import models
from .bolumler import Bolumler

class Dersler(models.Model):
    ders_adi=models.CharField(max_length=25)
    bolum_id=models.ForeignKey('Bolumler', on_delete=models.CASCADE)

    def __str__(self):
        return "{}  {} - {}".format(self.ders_adi, self.id,self.bolum_id)