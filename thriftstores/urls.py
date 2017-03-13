from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from thriftstores import views

urlpatterns = [
    url(r'^thriftstores/$', views.thriftstore_list),
    url(r'^thriftstores/(?P<pk>[0-9]+)/$', views.thriftstore_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)