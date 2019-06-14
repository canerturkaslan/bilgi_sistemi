from django.db import models
from .bolumler import Bolumler

class Dersler(models.Model):
    ders_adi=models.CharField(max_length=25)
    ders_id=models.IntegerField(unique=True,primary_key=True)
    bolum_id=models.ForeignKey('Bolumler', on_delete=models.CASCADE)