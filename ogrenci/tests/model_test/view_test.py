from django.test import TestCase,Client
from ogrenci.views.views import home_page
from django.http import HttpRequest
from ogrenci.models.bolumler import Bolumler
from ogrenci.models.dersler import Dersler
from ogrenci.models.ogrenci import Ogrenci
from django.urls import reverse
import sys

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_get_status(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class NotDetailViewTests(TestCase):

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi,
        )
        return bolum_test

    def ogrenci_olustur(self, isim, soyisim, bolum,telefon):

        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum=bolum,
            telefon=telefon)
        return ogrenci_test

    def ders_olustur(self, ders_adi, bolum):

        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum=bolum)
        return ders_test


    def test_post(self):
        bolum = self.bolum_olustur("fizik")
        ogrenci = self.ogrenci_olustur("caner", "turkaslan", bolum, "+90 531 406 01 89")
        dersler= self.ders_olustur("matematik",bolum)
        c = Client()
        response = c.post('/add', {'ogrenci_id': ogrenci.id, 'dersler_id': dersler.id,'puan':-5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ogrenci.objects.filter(isim='caner').count(), 1)

    def test_post_detail_404(self):
        response = self.client.get('/add/', args=(sys.maxsize))
        self.assertEqual(response.status_code, 404)
