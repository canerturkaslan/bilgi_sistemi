from django.contrib import admin
from .models.bolumler import Bolumler
from .models.dersler import Dersler
from .models.ogrenci import Ogrenci
from .models.ogrenci_notlar import Notlar
# Register your models here.
admin.site.register(Bolumler)
admin.site.register(Ogrenci)
admin.site.register(Dersler)
admin.site.register(Notlar)
