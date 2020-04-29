from rest_framework import viewsets

from wine_reviews.models import Wine
from wine_reviews.filters import WineFilter
from wine_reviews.serializers import WineSerializer


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all().order_by('-pk')
    serializer_class = WineSerializer
    filterset_class = WineFilter
