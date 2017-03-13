from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from thriftstores import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^thriftstores/$', views.ThriftStoreList.as_view()),
    url(r'^thriftstores/(?P<pk>[0-9]+)/$', views.ThriftStoreDetail.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)