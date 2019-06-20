from rest_framework import serializers
from ogrenci.models.ogrenci import Ogrenci


class OgrenciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogrenci

        fields = ('isim','soyisim','bolum','telefon')

        def validate_telefon(self, value):
            if value['not_valid']:
                raise serializers.ValidationError("Not valid")
            return value
