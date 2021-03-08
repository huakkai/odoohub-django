from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restf import views

urlpatterns = [
    url(r'^s/$', views.SnippetList.as_view()),
    url(r'^s/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
