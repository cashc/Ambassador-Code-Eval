from .models import Link
from rest_framework import viewsets
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all().order_by('id')
    serializer_class = LinkSerializer
