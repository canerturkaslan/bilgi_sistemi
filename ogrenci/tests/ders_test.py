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

    def test_validate_ders_adi(self):
        ders_adi = 3
        ders_id=2
        bolum_id=5
        self.ders_olustur(ders_adi,ders_id,bolum_id)
        assert isinstance(ders_adi,str),"ders adi is not a string"

    def test_validate_ders_id(self):
        ders_adi = "matematik"
        ders_id = "2"
        bolum_id = 5
        self.ders_olustur(ders_adi, ders_id, bolum_id)
        assert isinstance(ders_id ,int), "ders_id is not an integer"

    def test_validate_bolum_id(self):
        ders_adi = "programlama"
        ders_id = 2
        bolum_id = "65"
        self.ders_olustur(ders_adi, ders_id, bolum_id)
        assert isinstance(bolum_id,int), "bolum_id is not an integer"
