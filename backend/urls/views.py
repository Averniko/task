from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from urls.models import Url
from urls.serializers import UrlSerializer


class UrlView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]
