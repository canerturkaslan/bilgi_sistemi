from django.db import models
from .bolumler import Bolumler


class Ogrenci(models.Model):
    isim = models.CharField(max_length=15)
    soyisim = models.CharField(max_length=25)
    ogrenci_id = models.IntegerField(unique=True, primary_key=True)
    bolum_id = models.ForeignKey('Bolumler',on_delete=models.CASCADE)

    def __str__(self):
        return {self.isim}, {self.soyisim},{self.ogrenci_id},{self.bolum_id}