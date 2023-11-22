from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import Attachment, Course

import logging

logger = logging.getLogger(__name__)



class AttachmentSerializer(serializers.ModelSerializer):
    
    courseID = serializers.UUIDField(source='courseInfo.uid', required=False)

    class Meta:
        model = Attachment
        fields = ('uid', "name", 'url', 'courseID', 'createdAt', 'updateAt')


    def create(self, validated_data):
        courses_data = validated_data.pop('courseInfo', None)
        if courses_data is not None:
            course_instance = Course.objects.get(uid=courses_data['uid'])
            attachment_instance = Attachment.objects.create(courseInfo=course_instance, **validated_data)
            return attachment_instance
        

    def update(self, instance, validated_data):
        
        courses_data = validated_data.pop('courseInfo', None)
        if courses_data is not None:
            instance.courseInfo = Course.objects.get(uid=courses_data['uid'])
        
        instance.name = validated_data.get('name', instance.name)
        instance.url = validated_data.get('url', instance.url)
        
        instance.save()
        return instance