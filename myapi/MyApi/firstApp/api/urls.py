from django.conf.urls import url
from django.urls.conf import include
from .views import firstFunction
from rest_framework.routers import DefaultRouter
from .views import CarSpecsViewSet


router = DefaultRouter()
router.register('car-specs', CarSpecsViewSet, basename='car-specs')

urlpatterns = [
    url('first', firstFunction),
    url('', include(router.urls))
]
