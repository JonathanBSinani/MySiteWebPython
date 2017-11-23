from django.conf.urls import url

from apps.palestras.views import index_palestras

urlpatterns = [
    url(r'^index$', index_palestras),
]