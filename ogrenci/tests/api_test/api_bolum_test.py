from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from tastypie.test import *
from rest_framework.views import status
from ogrenci.models.bolumler import Bolumler
from ogrenci.serializers.bolum_serializers import BolumSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bolum(bolum_adi=""):
        if bolum_adi != "":
            Bolumler.objects.create(bolum_adi=bolum_adi)

    def setUp(self):
        self.create_bolum("Felsefe")
        self.create_bolum("Fizik")



class GetAllBolumsTest(BaseViewTest):

    def test_get_all_bolum(self):
        response = self.client.get(
            reverse('bolumler-list', kwargs={"version": "v1"})
        )

        expected = Bolumler.objects.all()
        serialized = BolumSerializer(expected, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceTest(BaseViewTest,ResourceTestCaseMixin,APITestCase):

    def create_bolum(self, bolum_adi="only a test"):
        return Bolumler.objects.create(bolum_adi=bolum_adi)

    def test_bolum_creation(self):
        w = self.create_bolum()
        self.assertTrue(isinstance(w, Bolumler))
        self.assertEqual(w.__str__(), w.bolum_adi)


    def test_post_api_json(self):
        client = APIClient()
        client.post('/api/v1/bolum/', {'bolum_adi': 'matematik'}, format='json')

    def test_create_bolum_api(self):

        url = '/api/v1/bolum/'
        data = {'bolum_adi': 'Bccs'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bolumler.objects.count(), 3)
        test_db=Bolumler.objects.get(bolum_adi="Bccs")
        self.assertEqual(test_db.bolum_adi, 'Bccs')

    def test_delete_bolum_api(self):
        url='/api/v1/bolum/1/'
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Bolumler.objects.count(), 1)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_bolum_api(self):
        url = '/api/v1/bolum/1/'
        data = {'bolum_adi': 'put test'}
        response = self.client.put(url,data)
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_db=Bolumler.objects.get(bolum_adi="put test")
        self.assertEqual("put test",test_db.bolum_adi)









