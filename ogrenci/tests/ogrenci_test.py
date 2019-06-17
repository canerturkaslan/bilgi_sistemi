from django.test import TestCase,RequestFactory
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.ogrenci import Ogrenci


class OgrenciModelTestCase(TestCase):

    def bolum_olustur(self,bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi)
        return bolum_test


    def ogrenci_olustur(self,isim,soyisim,bolum_id):
        bolum_id=self.bolum_olustur("elektronik muhendisligi")
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum_id=bolum_id)
        return ogrenci_test


    def test_validate_isim(self):
        isim=5
        soyisim="Turkaslan"
        bolum_id=2
        self.ogrenci_olustur(isim,soyisim,bolum_id)
        assert isinstance(isim, str),"isim is not a string: %r" % isim

    def test_validate_soyisim(self):
        isim="Caner"
        soyisim=4
        bolum_id=3
        self.ogrenci_olustur(isim,soyisim,bolum_id)
        assert isinstance(soyisim, str),"soyisim is not a string: %r" % soyisim

    def test_validate_bolum_id(self):
        isim="Caner"
        soyisim="Turkaslan"
        bolum_id="2"
        self.ogrenci_olustur(isim,soyisim,bolum_id)
        assert isinstance(bolum_id, int),"id is not an integer: %r" % bolum_id



