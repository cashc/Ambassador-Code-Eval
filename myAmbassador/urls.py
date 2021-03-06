from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^landing/$', views.landing)
]