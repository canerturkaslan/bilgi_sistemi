from rest_framework import serializers
from ogrenci.models.dersler import Dersler,Bolumler


class DersSerializer(serializers.ModelSerializer):
    bolum = serializers.SlugRelatedField(queryset=Bolumler.objects.all(), slug_field='bolum_adi')

    class Meta:
        model = Dersler
        fields = ('ders_adi','id','bolum')

