from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from thriftstores.models import ThriftStore
from thriftstores.serializers import ThriftStoreSerializer

"""
Note that because we want to be able to POST to this view from clients
that won't have a CSRF token we need to mark the view as csrf_exempt.
This isn't something that you'd normally want to do, and REST framework
views actually use more sensible behavior than this, but it'll do for our
purposes right now.
"""
@csrf_exempt
def thriftstore_list(request):
    """
    List all thriftstores, or create a new thriftstore.
    """
    if request.method == 'GET':
        thriftstores = ThriftStore.objects.all()
        serializer = ThriftStoreSerializer(thriftstores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ThriftStoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def thriftstore_detail(request, pk):
    """
    Retrieve, update or delete a thriftstore.
    """
    try:
        thriftstore = ThriftStore.objects.get(pk=pk)
    except ThriftStore.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ThriftStoreSerializer(thriftstore)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ThriftStoreSerializer(thriftstore, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        thriftstore.delete()
        return HttpResponse(status=204)