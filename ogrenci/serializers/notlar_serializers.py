from rest_framework import serializers
from ogrenci.models.ogrenci_notlar import Notlar,Ogrenci,Dersler



class NotlarSerializer(serializers.ModelSerializer):
    dersler=serializers.SlugRelatedField(queryset=Dersler.objects.all(),slug_field='ders_adi')
    ogrenci = serializers.SlugRelatedField(queryset=Ogrenci.objects.all(), slug_field='isim')
    class Meta:
        model = Notlar
        fields = ('dersler','ogrenci','puan')