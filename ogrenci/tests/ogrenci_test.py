from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.ogrenci import Ogrenci


class OgrenciModelTestCase(TestCase):

    def bolum_olustur(self,bolum_adi,bolum_id):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi,
            bolum_id=bolum_id)
        return bolum_test


    def ogrenci_olustur(self,isim,soyisim,ogrenci_id,bolum_id):
        bolum_id=self.bolum_olustur("elektronik muhendisligi",2)
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            ogrenci_id=ogrenci_id,
            bolum_id=bolum_id)
        return ogrenci_test


