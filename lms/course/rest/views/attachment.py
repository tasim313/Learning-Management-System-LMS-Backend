from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from ...models import Attachment
from ..serializers import attachment

import logging

logger = logging.getLogger(__name__)


class AttachmentList(generics.ListCreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = attachment.AttachmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uid', 'name', 'courseInfo__uid']


class AttachmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = attachment.AttachmentSerializer
    lookup_field = "uid"

    def perform_update(self, serializer):
        try:
            instance = serializer.save()
            
            logger.debug("Updated Attachment instance: %s", instance.__dict__)
        except Exception as e:
            logger.error("Error updating Attachment instance: %s", e)
            raise
