from thriftstores.models import ThriftStore
from thriftstores.serializers import ThriftStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from thriftstores.permissions import IsAdminOrReadOnly


class ThriftStoreList(APIView):
    """
    List all thriftstores, or create a new thriftstore.
    """
    def get(self, request, format=None):
        thriftstores = ThriftStore.objects.all()
        serializer = ThriftStoreSerializer(thriftstores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ThriftStoreSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly, )
        #print(request.data)
        if serializer.is_valid() and permission_classes:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThriftStoreDetail(APIView):
    """
    Retrieve, update or delete a thriftstore instance.
    """
    def get_object(self, pk):
        try:
            return ThriftStore.objects.get(pk=pk)
        except ThriftStore.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        thriftstore = self.get_object(pk)
        serializer = ThriftStoreSerializer(thriftstore)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        thriftstore = self.get_object(pk)
        serializer = ThriftStoreSerializer(thriftstore, data=request.data)
        if serializer.is_valid() and permission_classes:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        thriftstore = self.get_object(pk)
        thriftstore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)