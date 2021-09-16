from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import CarsAPIView


urlpatterns = [
    url('cars', CarsAPIView.as_view())
]
