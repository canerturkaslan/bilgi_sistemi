from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from tastypie.test import *
from rest_framework.views import status
from ogrenci.models.dersler import Dersler,Bolumler
from ogrenci.serializers.ders_serializers import DersSerializer

class BaseDersViewTest(APITestCase):
    client = APIClient()

    def bolum_olustur(self, bolum_adi):
        bolum_test = Bolumler.objects.create(
            bolum_adi=bolum_adi)
        return bolum_test

    def ders_olustur(self, ders_adi, bolum):
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum=bolum)
        return ders_test


    def setUp(self):
        bolum=self.bolum_olustur("Bilgisayar Muh")
        self.ders_olustur("Programlama",bolum)
        bolum = self.bolum_olustur("Elektronik Muh")
        self.ders_olustur("Statik", bolum)



class GetAllDersTest(BaseDersViewTest):

    def test_get_all_ders(self):
        response = self.client.get(
            reverse('dersler-list', kwargs={"version": "v1"})
        )

        expected = Dersler.objects.all()
        serialized = DersSerializer(expected, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceDersTest(BaseDersViewTest,ResourceTestCaseMixin,APITestCase):

    def test_ders_creation(self):
        bolum=self.bolum_olustur("Mekatronik Muh")
        w = self.ders_olustur("Programlama",bolum)
        self.assertTrue(isinstance(w, Dersler))
        object_to_string=str(w)
        self.assertEqual(w.__str__(),object_to_string)


    def test_post_ders_api_json(self):
        client = APIClient()
        client.post('/api/v1/ders/', {'bolum_adi': 'matematik'}, format='json')

    def test_create_ders_api(self):

        url = '/api/v1/ders/'
        data = {'bolum': 2,'ders_adi':"Devre"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dersler.objects.count(), 3)
        test_db=Dersler.objects.get(ders_adi="Devre")
        self.assertEqual(test_db.ders_adi, 'Devre')

    def test_delete_ders_api(self):
        url='/api/v1/ders/1/'
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Dersler.objects.count(), 1)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_ders_api(self):
        url = '/api/v1/ders/1/'
        data = {'bolum': 2,'ders_adi':"Felsefe"}
        response = self.client.put(url,data)
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_db=Dersler.objects.get(bolum=2,ders_adi="Felsefe")#BURDA KALDI DERS ADI PUT
        self.assertEqual(2,test_db.bolum_id)
        self.assertEqual("Felsefe",test_db.ders_adi)









