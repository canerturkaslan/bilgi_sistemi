from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .dersler import Dersler
from .ogrenci import Ogrenci


class Notlar(models.Model):
    ogrenci_id = models.ForeignKey('Ogrenci', on_delete=models.CASCADE)
    ders_id = models.ForeignKey('Dersler', on_delete=models.CASCADE)
    puan = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return "{}  {} - {}".format(self.ogrenci_id, self.ders_id,self.puan)