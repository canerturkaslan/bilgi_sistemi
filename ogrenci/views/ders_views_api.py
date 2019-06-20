from ogrenci.models import Dersler
from ogrenci.serializers.ders_serializers import DersSerializer
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet


class DersViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 bolum
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,
                     DestroyModelMixin):  # handles GETs for many bolum

      serializer_class = DersSerializer
      queryset = Dersler.objects.all()