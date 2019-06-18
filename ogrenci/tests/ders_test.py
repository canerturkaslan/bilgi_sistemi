from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler

class DerslerModelTestCase(TestCase):

    def bolum_olustur(self,bolum_adi):
        bolum_test=Bolumler.objects.create(
            bolum_adi=bolum_adi
        )
        return bolum_test

    def ders_olustur(self,ders_adi,bolum):
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum_id=bolum)
        return ders_test


