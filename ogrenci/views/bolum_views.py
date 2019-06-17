from rest_framework import generics
from ogrenci.models import Bolumler
from ogrenci.serializers.bolum_serializers import BolumSerializer


class ListBolumsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Bolumler.objects.all()
    serializer_class = BolumSerializer