from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

from ...models import Category
from ..serializers import category


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = category.CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid', 'name']


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = category.CategorySerializer
    lookup_field = "uid"