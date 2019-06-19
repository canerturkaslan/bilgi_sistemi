from ogrenci.models import Bolumler
from ogrenci.serializers.bolum_serializers import BolumSerializer
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet


class BolumViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 bolum
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,
                     DestroyModelMixin):  # handles GETs for many bolum

      serializer_class = BolumSerializer
      queryset = Bolumler.objects.all()