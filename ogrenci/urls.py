from ogrenci.views.bolum_views_api import BolumViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bolum', BolumViewSet,base_name='bolumler')

urlpatterns = router.urls