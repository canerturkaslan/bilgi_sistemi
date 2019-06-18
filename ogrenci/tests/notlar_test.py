from ogrenci.models.ogrenci_notlar import Notlar
from django.test import TestCase, RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler
from ogrenci.models.ogrenci import Ogrenci
import unittest


class NotlarModelTestCase(TestCase):

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi,
        )
        return bolum_test

    def ogrenci_olustur(self, isim, soyisim, bolum,telefon):

        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum=bolum,
            telefon=telefon)
        return ogrenci_test

    def ders_olustur(self, ders_adi, bolum):
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum=bolum)
        return ders_test

    def not_olustur(self, ogrenci, dersler, puan):
        puan = puan
        notlar_test = Notlar.objects.create(
            ogrenci=ogrenci,
            dersler=dersler,
            puan=puan)
        return notlar_test

    def test_validate_puan_range(self):
        bolum = self.bolum_olustur("fizik")
        dersler = self.ders_olustur("matematik",bolum)
        puan = -5
        ogrenci = self.ogrenci_olustur("caner","türkaslan",bolum,"+90 (531) 406 01 89")
        self.not_olustur(ogrenci, dersler, puan)
        assert not 100 >= puan >= 0, "Puan , Can not be less than 0 and Cannot be greater than 100"

    def test_validate_puan(self):
        bolum = self.bolum_olustur("fizik")
        dersler = self.ders_olustur("matematik", bolum)
        puan = "5"
        ogrenci = self.ogrenci_olustur("caner","türkaslan",bolum,"+90 (531) 406 01 89")
        self.not_olustur(ogrenci, dersler, puan)
        assert not isinstance(puan, int), "id is not an integer: %r" % puan