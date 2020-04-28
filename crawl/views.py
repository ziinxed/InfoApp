from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from crawl.models import Links
from crawl.serializers import LinksSerializer

@csrf_exempt
def link_list(request):
    if request.method == 'GET':
        links = Links.objects.all()
        serializer = LinksSerializer(links, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LinksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def link_detail(request, pk):

    try:
        link = Links.objects.get(pk=pk)
    except Links.DoesNotExist:
        return httpResponse(status=404)
    
    if request.method == 'GET':
        serializer = LinksSerializer(link)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JsonParser().parse(request)
        serializer = LinksSerializer(link, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResoponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        link.delete()
        return HttpResponse(status=204)


# Create your views here.
