from django.urls import path
from ogrenci.views.bolum_views_api import ListBolumsView

urlpatterns = [
    path('bolums/', ListBolumsView.as_view(), name="bolums-all")
]
