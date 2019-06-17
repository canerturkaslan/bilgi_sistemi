
"""from django.urls import path
# from ogrenci.views.bolum_views import  ListBolumsView

urlpatterns = [

 #   path('bolums/', ListBolumsView.as_view(), name="bolums-all")
]"""


from django.conf.urls import url
from ogrenci import views
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]