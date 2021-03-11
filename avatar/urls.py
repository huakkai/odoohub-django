from django.conf.urls import url
from django.urls import path
from . import views
from odoohub_django import settings
from django.views.static import serve


urlpatterns = [
    path('upload/', views.upload),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
