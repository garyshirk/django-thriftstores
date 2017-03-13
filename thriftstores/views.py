from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from thriftstores.models import ThriftStore
from thriftstores.serializers import ThriftStoreSerializer

"""
Note that because we want to be able to POST to this view from clients
that won't have a CSRF token we need to mark the view as csrf_exempt.
This isn't something that you'd normally want to do, and REST framework
views actually use more sensible behavior than this, but it'll do for our
purposes right now.
"""
@api_view(['GET', 'POST'])
def thriftstore_list(request, format=None):
    """
    List all thriftstores, or create a new thriftstore.
    """
    if request.method == 'GET':
        thriftstores = ThriftStore.objects.all()
        serializer = ThriftStoreSerializer(thriftstores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThriftStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def thriftstore_detail(request, pk, format=None):
    """
    Retrieve, update or delete a thriftstore.
    """
    try:
        thriftstore = ThriftStore.objects.get(pk=pk)
    except ThriftStore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ThriftStoreSerializer(thriftstore)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ThriftStoreSerializer(thriftstore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        thriftstore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
