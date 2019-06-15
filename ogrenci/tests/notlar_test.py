from ogrenci.models.ogrenci_notlar import Notlar
from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler
from ogrenci.models.ogrenci import Ogrenci
from ogrenci.tests.bolum_test import *

class NotlarModelTestCase(TestCase):


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

    def ders_olustur(self,ders_adi,ders_id,bolum_id):
        bolum_id=self.bolum_olustur("bilgisayar muhendisligi", 1)
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            ders_id=ders_id,
            bolum_id=bolum_id)
        return ders_test

    def not_olustur(self,ogrenci_id,ders_id,puan):
        ogrenci_id=self.ogrenci_olustur("caner", "veli", 1, 3)
        ders_id=self.ders_olustur("matematik", 2, 1)
        notlar_test = Notlar.objects.create(
            ogrenci_id=ogrenci_id,
            ders_id=ders_id,
            puan=45)
        return notlar_test







