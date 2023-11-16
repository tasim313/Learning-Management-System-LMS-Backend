from rest_framework import serializers

from ...models import Category

import logging

logger = logging.getLogger(__name__)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uid', 'name')