from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from tastypie.test import *
from rest_framework.views import status
from ogrenci.models import Ogrenci,Dersler,Notlar,Bolumler
from ogrenci.serializers.notlar_serializers import NotlarSerializer

class BaseNotlarViewTest(APITestCase):
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

    def ders_olustur(self, ders_adi, bolum):
        ders_test = Dersler.objects.create(
            ders_adi=ders_adi,
            bolum=bolum)
        return ders_test

    def not_olustur(self,ogrenci,dersler,puan):
        notlar_test=Notlar.objects.create(
            ogrenci=ogrenci,
            dersler=dersler,
            puan=puan
        )
        return notlar_test

    def setUp(self):

        bolum=self.bolum_olustur("Bilgisayar Muh")
        ogrenci=self.ogrenci_olustur("Caner","Turkaslan",bolum,"+90 (531) 406 01 89")
        bolumtest_2 = self.bolum_olustur("Elektronik Muh")
        ogrencitest_2=self.ogrenci_olustur("Ali","Veli",bolumtest_2,"+90 (552) 887 23 73")
        ders=self.ders_olustur("Statik", bolum)
        derstest_2=self.ders_olustur("Devre", bolum)
        self.not_olustur(ogrenci,ders,45)
        self.not_olustur(ogrencitest_2,derstest_2,78)


class GetAllNotlarTest(BaseNotlarViewTest):

    def test_get_all_notlar(self):
        response = self.client.get(
            reverse('notlar-list', kwargs={"version": "v1"})
        )

        expected = Notlar.objects.all()
        serialized = NotlarSerializer(expected, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EntryResourceNotlarTest(BaseNotlarViewTest,ResourceTestCaseMixin,APITestCase):

    def test_not_creation(self):
        bolum=self.bolum_olustur("Mekatronik Muh")
        ogrenci=self.ogrenci_olustur("Caner","Turkaslan",bolum,"+90 (531) 406 01 89")
        ders = self.ders_olustur("Statik", bolum)
        w=self.not_olustur(ogrenci, ders, 45)
        self.assertTrue(isinstance(w, Notlar))
        object_to_string=str(w)
        self.assertEqual(w.__str__(),object_to_string)

    def test_post_not_api_json(self):
        client = APIClient()
        response = client.post('/api/v1/not/', {'dersler': 2,'ogrenci':2,'puan':12}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_not_api(self):

        url = '/api/v1/not/'
        data = {'dersler': 1,'ogrenci':1,'puan':23}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notlar.objects.count(), 3)
        test_db=Notlar.objects.get(puan=23)
        self.assertEqual(test_db.puan, 23)

    def test_delete_not_api(self):
        url='/api/v1/not/1/'
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Notlar.objects.count(), 1)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_not_api(self):
        url = '/api/v1/not/1/'
        data = {'ogrenci':2,'dersler':2,'puan':44}
        response = self.client.put(url,data)
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test_db=Notlar.objects.get(id=1)
        self.assertEqual(2,test_db.ogrenci_id)
        self.assertEqual(44,test_db.puan)
        self.assertEqual(2,test_db.dersler_id)








