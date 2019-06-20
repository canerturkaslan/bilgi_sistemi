from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .dersler import Dersler
from .ogrenci import Ogrenci


class Notlar(models.Model):
    ogrenci = models.ForeignKey('Ogrenci', on_delete=models.CASCADE)
    dersler = models.ForeignKey('Dersler', on_delete=models.CASCADE)
    puan = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return "{}  {} - {}".format(self.ogrenci, self.dersler,self.puan)