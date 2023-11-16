from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import Course, CourseCollectionBridge

import logging

logger = logging.getLogger(__name__)



class CourseCollectionBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCollectionBridge
        fields = ('category', 'courses')




class CourseSerializer(serializers.ModelSerializer):
    
    categories = CourseCollectionBridgeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'uid', 'userId', 'description', 'imageUrl', 'price', 'isPublished', 'categories', 'createdAt', 'updateAt')

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        course = Course.objects.create(**validated_data)
        for category_data in categories_data:
            CourseCollectionBridge.objects.create(course=course, **category_data)
        return course

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.userId = validated_data.get('userId', instance.userId)
        instance.description = validated_data.get('description', instance.description)
        instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
        instance.price = validated_data.get('price', instance.price)
        instance.isPublished = validated_data.get('isPublished', instance.isPublished)
        instance.save()

        # Handle many-to-many relationships
        categories_data = validated_data.get('categories', [])
        instance.categories.all().delete()  # Remove existing categories
        for category_data in categories_data:
            CourseCollectionBridge.objects.create(course=instance, **category_data)

        return instance