from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

from ...models import Course
from ..serializers import course

import logging

logger = logging.getLogger(__name__)


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = course.CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid', 'userId']


class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = course.CourseSerializer
    lookup_field = "uid"
