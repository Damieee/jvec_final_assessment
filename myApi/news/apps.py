# news/api.py

from rest_framework import viewsets
from .models import NewsItem
from .serializers import NewsItemSerializer

class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
