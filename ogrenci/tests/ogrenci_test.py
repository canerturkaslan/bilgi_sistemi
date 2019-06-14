from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.ogrenci import Ogrenci


class OgrenciModelTestCase(TestCase):
    def test_setUp(self):
        self.factory = RequestFactory()
        bolum_test=Bolumler.objects.create(
            bolum_adi="deneme",
            bolum_id=1
        )
        self.ogrenci_test=Ogrenci.objects.create(
                isim="mark",
                soyisim="ali",
                ogrenci_id=1,
                bolum_id=bolum_test)



