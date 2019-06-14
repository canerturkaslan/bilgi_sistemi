from django.test import TestCase,RequestFactory
from .models.bolumler import Bolumler
from .models.dersler import Dersler
from .models.ogrenci import Ogrenci
from .models.ogrenci_notlar import Notlar


class BolumModelTestCase(TestCase):
    def test_setUp(self):
        self.factory = RequestFactory()
        self.bolum_test=Bolumler.objects.create(
            bolum_adi="deneme",
            bolum_id=1
        )


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


class NotlarModelTestCase(TestCase):
    def test_setUp(self):
        bolum_test = Bolumler.objects.create(
            bolum_adi="deneme",
            bolum_id=1
        )
        ogrenci_test = Ogrenci.objects.create(
            isim="mark",
            soyisim="ali",
            ogrenci_id=1,
            bolum_id=bolum_test)
        ders_test=Dersler.objects.create(
            ders_adi="matematik",
            ders_id=1,
            bolum_id=bolum_test
        )
        self.notlar_test=Notlar.objects.create(
            ogrenci_id=ogrenci_test,
            ders_id=ders_test,
            puan=45)
