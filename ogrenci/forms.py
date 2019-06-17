from django import forms


class NotForm(forms.Form):
    ders_id = forms.IntegerField()
    ogrenci_id = forms.IntegerField()
    puan = forms.IntegerField()