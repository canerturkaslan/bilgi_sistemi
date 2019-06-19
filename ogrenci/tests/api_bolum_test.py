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
        self.client.login(username="caner", password="caner292")
        self.create_bolum("Felsefe")
        self.create_bolum("Fizik")
        self.create_bolum("Bilgisayar Muh")


class GetAllBolumsTest(BaseViewTest):

    def test_get_all_bolum(self):
        response = self.client.get(
            reverse("bolums-all", kwargs={"version": "v1"})
        )

        expected = Bolumler.objects.all()
        serialized = BolumSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceTest(ResourceTestCaseMixin,APITestCase):

    def create_bolum(self, bolum_adi="only a test"):
        return Bolumler.objects.create(bolum_adi=bolum_adi)

    def test_bolum_creation(self):
        w = self.create_bolum()
        self.assertTrue(isinstance(w, Bolumler))
        self.assertEqual(w.__str__(), w.bolum_adi)

    def test_get_api_json(self):
        self.client.login(username="test", password="test")
        resp = self.api_client.get('/api/v1/bolums/', format='json')
        self.assertValidJSONResponse(resp)

    def test_bolum_authorization(self):
        self.client.login(username="test", password="test")
        response = self.client.get('/api/v1/bolums/')
        self.assertEqual(403, response.status_code)

""" AUTHENTICATION DA KALDI,ONDAN SONRA CREATEAPIVIEW VE DELETE API VIEW BAKIP TEST YAZ AMA AUTHENTICATION ONEMLI"""