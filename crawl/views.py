from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crawl.models import Links
from crawl.serializers import LinksSerializer


@api_view(['GET', 'POST'])
def link_list(request, format = None):
    """
    List all code snippets, or create a new link.
    """
    if request.method == 'GET':
        snippets = Links.objects.all()
        serializer = LinksSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def link_detail(request, pk, format = None):
    """
    Retrieve, update or delete a link.
    """
    try:
        snippet = Links.objects.get(pk=pk)
    except Links.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LinksSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LinksSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
