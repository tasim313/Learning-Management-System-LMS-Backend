from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import Course

import logging

logger = logging.getLogger(__name__)



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'uid', 'userId', 'description', 'imageUrl', 'price', 'isPublished', 'categories', 'createdAt', 'updateAt')