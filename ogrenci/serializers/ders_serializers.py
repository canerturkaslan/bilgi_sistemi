from rest_framework import serializers
from ogrenci.models.dersler import Dersler


class DersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dersler
        fields = ('ders_adi','id','bolum')