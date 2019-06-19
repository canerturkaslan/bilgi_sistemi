from django.test import TestCase
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.ogrenci import Ogrenci
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
        test.save()
        self.assertRaises(ValidationError, test.full_clean)
        self.assertEqual(Ogrenci.objects.filter(isim='Caner').count(), 1)

    """def test_telefon_regex_not(self):
        bolum=self.bolum_olustur("matematik")
        telefon="5314060189"
        test=self.ogrenci_olustur("caner", "turkaslan", bolum, telefon)
        test.save()
        self.assertRaises(ValidationError, test.full_clean)"""

















