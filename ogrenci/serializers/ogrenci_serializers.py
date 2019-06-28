from rest_framework import serializers
from ogrenci.models.ogrenci import Ogrenci,Bolumler



class OgrenciSerializer(serializers.ModelSerializer):
    bolum = serializers.SlugRelatedField(queryset=Bolumler.objects.all(), slug_field='bolum_adi')

    class Meta:
        model = Ogrenci
        fields = ('isim','soyisim','bolum','telefon')

        def validate_telefon(self, value):
            if value['not_valid']:
                raise serializers.ValidationError("Not valid")
            return value
