from django.db import models


class Bolumler(models.Model):
    bolum_adi=models.CharField(max_length=20)

    def __str__(self):
        return self.bolum_adi
