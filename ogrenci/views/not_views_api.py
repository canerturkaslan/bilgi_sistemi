from ogrenci.models import Notlar
from ogrenci.serializers.notlar_serializers import NotlarSerializer
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet


class NotlarViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 bolum
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin,
                     DestroyModelMixin):  # handles GETs for many bolum

      serializer_class = NotlarSerializer
      queryset = Notlar.objects.all()