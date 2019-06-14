from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler

class DerslerModelTestCase(TestCase):
    def test_setUp(self):
        self.factory = RequestFactory()
        bolum_test = Bolumler.objects.create(
            bolum_adi="deneme",
            bolum_id=1
        )
        self.ders_test=Dersler.objects.create(
            ders_adi="matematik",
            ders_id=1,
            bolum_id=bolum_test
        )