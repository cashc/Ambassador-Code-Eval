from django.http import HttpResponse, JsonResponse
from .models import Link
from rest_framework import viewsets
from .serializers import LinkSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all().order_by('id')
    serializer_class = LinkSerializer

    @csrf_exempt
    def link_list(request):
        """
        List all code links, or create a new link.
        """
        if request.method == 'GET':
            links = Link.objects.all()
            serializer = LinkSerializer(links, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = LinkSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def link_detail(request, pk):
        """
        Retrieve, update or delete a code link.
        """
        try:
            link = Link.objects.get(pk=pk)
        except Link.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = LinkSerializer(link)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = LinkSerializer(link, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            link.delete()
            return HttpResponse(status=204)

@csrf_exempt
def landing(request):
    """
    Increment the link if found
    """
    title = request.GET.get('link')
    print("title: ",title)
    try:
        link = Link.objects.get(title=title)
    except Link.DoesNotExist:
        return HttpResponse(content="Tim wants to do some marketing!",status=204)

    link.clicks += 1
    Link.save(link)
    print(link.title,":",link.clicks)
    return HttpResponse(content="That's {0}!<br>{1} are the bomb!".format(link.clicks,link.title),status=200)
