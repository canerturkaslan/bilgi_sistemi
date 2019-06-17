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
        # add test data
        self.create_bolum("Felsefe")
        self.create_bolum("Fizik")
        self.create_bolum("Besyo")


class GetAllBolumsTest(BaseViewTest):

    def test_get_all_bolum(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("bolums-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Bolumler.objects.all()
        serialized = BolumSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceTest(ResourceTestCaseMixin,APITestCase):

    def test_get_api_json(self):
        resp = self.api_client.get('/api/v1/bolums', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_api_xml(self):
        resp = self.api_client.get('/api/v1/bolums/', format='xml')
        self.assertValidXMLResponse(resp)