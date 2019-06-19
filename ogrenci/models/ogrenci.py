from django.db import models
from .bolumler import Bolumler
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_telefon(value):
    if re.match('^\+(\d{2})\s\((\d{3})\)\s(\d{3})\s(\d{2})\s(\d{2})', value):
        raise ValidationError('Disallowed Phone')



class Ogrenci(models.Model):
    isim = models.CharField(max_length=15)
    soyisim = models.CharField(max_length=25)
    bolum = models.ForeignKey('Bolumler', on_delete=models.CASCADE)
    telefon = models.CharField(max_length=19, validators=[RegexValidator(regex="^\+(\d{2})\s\((\d{3})\)\s(\d{3})\s(\d{2})\s(\d{2})")], null=True)

    def __str__(self):
        return "{}  {} {} - {}-{}".format(self.isim, self.soyisim, self.id, self.bolum,self.telefon)
