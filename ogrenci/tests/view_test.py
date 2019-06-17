from django.urls import resolve
from django.test import TestCase,Client
from ogrenci.views import home_page,add_not_page
from django.http import HttpRequest
from ogrenci.models.ogrenci_notlar import Notlar
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
        self.assertEquals(response.status_code, 200)


class NotDetailViewTests(TestCase):

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi,
        )
        return bolum_test

    def ogrenci_olustur(self, isim, soyisim, bolum_id):
        bolum_id = self.bolum_olustur("elektronik muhendisligi")
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum_id=bolum_id)
        return ogrenci_test

    def ders_olustur(self, ders_adi, bolum_id):
        bolum_id = self.bolum_olustur("bilgisayar muhendisligi")
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum_id=bolum_id)
        return ders_test

    def setUp(self):
        super(NotDetailViewTests, self).setUp()
        self.notlar = Notlar.objects.create(ders_id=self.ders_olustur("matematik",1),
                                            ogrenci_id=self.ogrenci_olustur("caner","turkaslan",1),
                                            puan=45)

    def tearDown(self):
        super(NotDetailViewTests, self).tearDown()
        self.notlar.delete()

    def test_add_not_success(self):
        response = self.client.get('/add/', args=(self.notlar.id,))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,self.notlar.id)

    def test_post_detail_404(self):
        response = self.client.get('/add/', args=(sys.maxsize,))
        self.assertEqual(response.status_code, 404)