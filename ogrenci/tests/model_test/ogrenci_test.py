from django.test import TestCase
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.ogrenci import Ogrenci,validate_telefon
from django.core.exceptions import ValidationError


class OgrenciModelTestCase(TestCase):
    def bolum_olustur(self,bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi)
        return bolum_test

    def ogrenci_olustur(self,isim,soyisim,bolum,telefon):
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum=bolum,
            telefon=telefon)
        return ogrenci_test

    def test_telefon_regex(self):
        bolum=self.bolum_olustur("matematik")
        telefon="+90 (531) 406 01 95"
        test=self.ogrenci_olustur("Caner","Turkaslan",bolum,telefon)
        self.assertRaises(ValidationError,test.full_clean())

    def test_telefon_regex_not(self):
        bolum=self.bolum_olustur("matematik")
        telefon="5314060189"
        self.ogrenci_olustur("caner", "turkaslan", bolum, telefon)
        self.assertRaises(ValidationError, validate_telefon(telefon))




















