from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler


class BolumModelTestCase(TestCase):
    def test_setUp(self):
        self.factory = RequestFactory()
        self.bolum_test=Bolumler.objects.create(
            bolum_adi="deneme",
            bolum_id=1
        )