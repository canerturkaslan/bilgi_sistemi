from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from tastypie.test import *
from rest_framework.views import status
from ogrenci.models import Ogrenci,Bolumler
from ogrenci.serializers.ogrenci_serializers import OgrenciSerializer

class BaseOgrenciViewTest(APITestCase):
    client = APIClient()

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi)
        return bolum_test

    def ogrenci_olustur(self,isim, soyisim, bolum,telefon):
        ogrenci_test = Ogrenci.objects.create(
            isim=isim,
            soyisim=soyisim,
            bolum=bolum,
            telefon=telefon)
        return ogrenci_test


    def setUp(self):
        bolum=self.bolum_olustur("Bilgisayar Muh")
        self.ogrenci_olustur("Caner","Turkaslan",bolum,"+90 (531) 406 01 89")
        bolum = self.bolum_olustur("Elektronik Muh")
        self.ogrenci_olustur("Ali","Veli",bolum,"+90 (552) 887 23 73")


class GetAllOgrenciTest(BaseOgrenciViewTest):

    def test_get_all_ogrenci(self):
        response = self.client.get(
            reverse('ogrenciler-list', kwargs={"version": "v1"})
        )

        expected = Ogrenci.objects.all()
        serialized = OgrenciSerializer(expected, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceOgrenciTest(BaseOgrenciViewTest,ResourceTestCaseMixin,APITestCase):

    def test_ogrenci_creation(self):
        bolum=self.bolum_olustur("Mekatronik Muh")
        w=self.ogrenci_olustur("Caner","Turkaslan",bolum,"+90 (531) 406 01 89")
        self.assertTrue(isinstance(w, Ogrenci))
        object_to_string=str(w)
        self.assertEqual(w.__str__(),object_to_string)

    def test_post_ogrenci_api_json(self):
        client = APIClient()
        response = client.post('/api/v1/ogrenci/', {'isim': 'caner','soyisim':'turkaslan','bolum':2,'telefon':'+90 (531) 406 01 89'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_ogrenci_api(self):

        url = '/api/v1/ogrenci/'
        data = {'isim': 'caner','soyisim':'turkaslan','bolum':2,'telefon':'+90 (531) 406 01 89'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ogrenci.objects.count(), 3)
        test_db=Ogrenci.objects.get(isim="caner")
        self.assertEqual(test_db.isim, 'caner')

    def test_delete_ogrenci_api(self):
        url='/api/v1/ogrenci/1/'
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Ogrenci.objects.count(), 1)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_ogrenci_api(self):
        url = '/api/v1/ogrenci/1/'
        data = {'isim':"Ali",'soyisim':"Veli","bolum":2,'telefon':"+90 (552) 887 23 73"}
        response = self.client.put(url,data)
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_db=Ogrenci.objects.get(id=1)
        self.assertEqual(2,test_db.bolum_id)
        self.assertEqual("Ali",test_db.isim)
        self.assertEqual("+90 (552) 887 23 73",test_db.telefon)









