from django.db import models

import uuid
from versatileimagefield.fields import VersatileImageField


from .utils import(
    get_course_image
)


class Category(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=100, db_index=True, blank=True, null=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    userId = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=500, db_index=True)
    description = models.TextField(blank=True, null=True)
    imageUrl = VersatileImageField(
        upload_to=get_course_image,
        null=True, blank=True)
    
    price = models.FloatField(blank=True, null=True)
    isPublished = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Attachment(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=200, db_index=True, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    courseInfo = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)