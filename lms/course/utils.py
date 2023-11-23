from uuid import uuid4
import logging

logger = logging.getLogger(__name__)

def get_course_image(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{instance.uid}{'image'}{instance.title}{uid}-{filename}"


def get_attachment_file(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"attachments/{uid}-{filename}"


def get_chapter_video_file(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"chapter/{uid}-{filename}"


def get_course_instance(uid):
    from django.core.exceptions import (
        ObjectDoesNotExist,
        MultipleObjectsReturned)
    from .models import Course
    try:
        instance = Course.objects.get(uid=uid)
        course = instance.id
        return course
    except MultipleObjectsReturned:
        instance = Course.objects.filter(uid=uid)[0]
        course = instance.id
        return course
    except ObjectDoesNotExist:
        logging.error("course does not exist")
    isinstance = Course.objects.filter(uid=uid)
    return isinstance.id