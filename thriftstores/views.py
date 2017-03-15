from thriftstores.models import ThriftStore
from thriftstores.serializers import ThriftStoreSerializer
from rest_framework import generics


class ThriftStoreList(generics.ListCreateAPIView):
    queryset = ThriftStore.objects.all()
    serializer_class = ThriftStoreSerializer


class ThriftStoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThriftStore.objects.all()
    serializer_class = ThriftStoreSerializer