from django.urls import path, include
from ogrenci.views import views
from django.conf.urls import url,re_path
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home'),
    path('add', views.add_not_page, name='add'),
    re_path('api/(?P<version>(v1|v2))/', include('ogrenci.urls'))
]
