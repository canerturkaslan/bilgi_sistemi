from ogrenci.views.bolum_views_api import BolumViewSet
from ogrenci.views.ders_views_api import DersViewSet
from ogrenci.views.ogrenci_views_api import OgrenciViewSet
from ogrenci.views.not_views_api import NotlarViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bolum', BolumViewSet,base_name='bolumler')
router.register(r'ders',DersViewSet,base_name='dersler')
router.register(r'ogrenci',OgrenciViewSet,base_name='ogrenciler')
router.register(r'not',NotlarViewSet,base_name='notlar')
urlpatterns = router.urls