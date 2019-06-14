from django.db import models


class Bolumler(models.Model):
    bolum_adi=models.CharField(max_length=20)
    bolum_id=models.IntegerField(unique=True, primary_key=True)
