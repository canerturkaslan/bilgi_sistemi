from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler

class DerslerModelTestCase(TestCase):

    def bolum_olustur(self,bolum_adi,bolum_id):
        bolum_test=Bolumler.objects.create(
            bolum_adi=bolum_adi,
            bolum_id=bolum_id)
        return bolum_test

    def ders_olustur(self,ders_adi,ders_id,bolum_id):
        bolum_id=self.bolum_olustur("bilgisayar muhendisligi", 1)
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            ders_id=ders_id,
            bolum_id=bolum_id)
        return ders_test