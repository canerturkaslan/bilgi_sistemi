from ogrenci.models import Ogrenci
from ogrenci.serializers.ogrenci_serializers import OgrenciSerializer
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet


class OgrenciViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 bolum
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,
                     DestroyModelMixin):  # handles GETs for many bolum

      serializer_class = OgrenciSerializer
      queryset = Ogrenci.objects.all()