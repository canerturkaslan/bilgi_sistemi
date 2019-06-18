from django.db import models
from .bolumler import Bolumler


class Dersler(models.Model):
    ders_adi=models.CharField(max_length=50)
    bolum=models.ForeignKey('Bolumler', on_delete=models.CASCADE)

    def __str__(self):
        return "{}  {} - {}".format(self.ders_adi, self.id,self.bolum)