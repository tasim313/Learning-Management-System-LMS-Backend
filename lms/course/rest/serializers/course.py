from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import Course, Category

import logging

logger = logging.getLogger(__name__)



class CourseSerializer(serializers.ModelSerializer):
    categoryId = serializers.UUIDField(source='categories.uid', required=False)

    class Meta:
        model = Course
        fields = ('title', 'uid', 'userId', 'description', 'imageUrl', 'price', 'isPublished', 'categoryId', 'createdAt', 'updateAt')

    def update(self, instance, validated_data):
        
        categories_data = validated_data.pop('categories', None)
        if categories_data is not None:
            instance.categories = Category.objects.get(uid=categories_data['uid'])
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
       
        instance.save()
        return instance
