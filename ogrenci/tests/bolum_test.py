from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler


class BolumModelTestCase(TestCase):


    def bolum_olustur(self,bolum_adi):
        Bolumler.objects.create(
            bolum_adi=bolum_adi,
         )


    def test_validate_bolum_adi(self):
            bolum_adi = 2
            self.bolum_olustur(bolum_adi)
            assert isinstance(bolum_adi, str), "bolum_adi is not a string : %r" % bolum_adi