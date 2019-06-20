from rest_framework import serializers
from ogrenci.models.ogrenci_notlar import Notlar


class NotlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notlar
        fields = ('dersler','ogrenci','puan')