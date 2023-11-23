from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


from ...models import Attachment, Course

import logging

logger = logging.getLogger(__name__)

from ...utils import get_course_instance



class AttachmentSerializer(serializers.Serializer):

    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    file = serializers.FileField()

    class Meta:
        fields = (
            'uid',
            'name',
            'file',
            'courseInfo',
            'createdAt',
            'updateAt',
        )
        read_only_fields = ('createdAt', 'updateAt')
        

    def create(self, validated_data):
        uid = validated_data.get('uid')
        file = validated_data.get('file')
        course = get_course_instance(uid)

        attachment = Attachment.objects.create(
            file=file,
            courseInfo_id=course,
        )

        return attachment

    

    def update(self, instance, validated_data):
        courses_data = validated_data.pop('courseInfo', None)
        if courses_data is not None:
            instance.courseInfo = Course.objects.get(uid=courses_data['uid'])
        
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)  
        
        instance.save()
        return instance