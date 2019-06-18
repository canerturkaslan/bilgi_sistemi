from ogrenci.models.ogrenci_notlar import Notlar
from django.test import TestCase, RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler
from ogrenci.models.ogrenci import Ogrenci
from ogrenci.tests.bolum_test import *
import unittest


class NotlarModelTestCase(TestCase):

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi,
        )
        return bolum_test

    def ogrenci_olustur(self, isim, soyisim, bolum_id):
        bolum_id = self.bolum_olustur("elektronik muhendisligi")
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum_id=bolum_id)
        return ogrenci_test

    def ders_olustur(self, ders_adi, bolum_id):
        bolum_id = self.bolum_olustur("bilgisayar muhendisligi")
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum_id=bolum_id)
        return ders_test

    def not_olustur(self, ogrenci_id, ders_id, puan):
        ogrenci_id = self.ogrenci_olustur("caner", "veli", 1 )
        ders_id = self.ders_olustur("matematik", 2)
        puan = puan
        notlar_test = Notlar.objects.create(
            ogrenci_id=ogrenci_id,
            ders_id=ders_id,
            puan=puan)
        return notlar_test

    def test_validate_ogrenci_id(self):
        ders_id = 2
        puan = 45
        ogrenci_id = "1"
        self.not_olustur(ogrenci_id, ders_id, puan)
        assert isinstance(ogrenci_id, int), "id is not an integer: %r" % ogrenci_id

    def test_validate_ders_id(self):
        ders_id = "2"
        puan = 45
        ogrenci_id = 1
        self.not_olustur(ogrenci_id, ders_id, puan)
        assert isinstance(ders_id, int), "id is not an integer: %r" % ders_id

    def test_validate_puan_range(self):
        ders_id = 2
        puan = -5
        ogrenci_id = 1
        self.not_olustur(ogrenci_id, ders_id, puan)
        assert 100 >= puan >= 0, "Puan , Can not be less than 0 and Cannot be greater than 100"

    def test_validate_puan(self):
        ders_id = 2
        puan = "5"
        ogrenci_id = 1
        self.not_olustur(ogrenci_id, ders_id, puan)
        assert isinstance(puan, int), "id is not an integer: %r" % puan
