from rest_framework import generics
from ogrenci.models import Bolumler
from ogrenci.serializers.bolum_serializers import BolumSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ListBolumsView(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Bolumler.objects.all()
    serializer_class = BolumSerializer