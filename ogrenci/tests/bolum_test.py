from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler


class BolumModelTestCase(TestCase):


    def bolum_olustur(self,bolum_adi,bolum_id):
        Bolumler.objects.create(
            bolum_adi=bolum_adi,
            bolum_id=bolum_id
        )


    def test_validate_bolum_id(self):
        bolum_adi="matematik"
        bolum_id="2"
        self.bolum_olustur(bolum_adi,bolum_id)
        assert isinstance(bolum_id, int) , "id is not an integer: %r" % bolum_id

    def test_validate_bolum_adi(self):
            bolum_adi = 2
            bolum_id = 1
            self.bolum_olustur(bolum_adi, bolum_id)
            assert isinstance(bolum_adi, str), "bolum_adi is not a string : %r" % bolum_adi