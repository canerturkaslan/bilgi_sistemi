from rest_framework import serializers
from ogrenci.models.bolumler import Bolumler


class BolumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolumler
        fields = ('bolum_adi','id')