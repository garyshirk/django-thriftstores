import django_filters
from rest_framework.filters import SearchFilter
from thriftstores.models import ThriftStore
from thriftstores.serializers import ThriftStoreSerializer
from rest_framework import generics
#from django_filters.rest_framework import DjangoFilterBackend

class ThriftStoreFilter(django_filters.rest_framework.FilterSet):
    east_long = django_filters.NumberFilter(name="locLong", lookup_expr='lt')
    west_long = django_filters.NumberFilter(name="locLong", lookup_expr='gt')
    north_lat = django_filters.NumberFilter(name="locLat", lookup_expr='lt')
    south_lat = django_filters.NumberFilter(name="locLat", lookup_expr='gt')

    #max_price = django_filters.NumberFilter(name="price", lookup_expr='lte')
    class Meta:
        model = ThriftStore
        fields = ['bizZip',]


class ThriftStoreList(generics.ListCreateAPIView):
    queryset = ThriftStore.objects.all()
    serializer_class = ThriftStoreSerializer
    filter_backends = (SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ThriftStoreFilter
    search_fields = ('^bizName', '^bizCity')


class ThriftStoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThriftStore.objects.all()
    serializer_class = ThriftStoreSerializer