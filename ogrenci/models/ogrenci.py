from django.db import models
from .bolumler import Bolumler


class Ogrenci(models.Model):
    isim = models.CharField(max_length=15)
    soyisim = models.CharField(max_length=25)
    bolum_id = models.ForeignKey('Bolumler',on_delete=models.CASCADE)

    def __str__(self):
        return "{}  {} {} - {}".format(self.isim, self.soyisim,self.id,self.bolum_id)