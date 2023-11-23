from django.db import models
from django.contrib.auth.models import User

import uuid
from versatileimagefield.fields import VersatileImageField


from .utils import(
    get_course_image,
    get_attachment_file,
    get_chapter_video_file
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
    file = models.FileField(upload_to=get_attachment_file, null=True, blank=True)
    courseInfo = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)


class Chapter(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=200, db_index=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    videoFile = models.FileField(upload_to=get_chapter_video_file, null=True, blank=True)
    position = models.IntegerField(blank=True, null=True)
    isPublished = models.BooleanField(default=False)
    isFree = models.BooleanField(default=False)
    course_chapter = models.ForeignKey(Course, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)



class MuxData(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    assetId = models.CharField(max_length=100, blank=True, null=True)
    playbackId = models.CharField(max_length=100, blank=True, null=True)
    chapter_mux_data = models.OneToOneField(Chapter, on_delete=models.CASCADE, related_name="mux_data_chapter")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)


class UserProgress(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    user_user_progress = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_progress_user")
    chapter_user_progress = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="user_progress_chapter")
    is_completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user_user_progress', 'chapter_user_progress']


class Purchase(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    user_purchase = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_user")
    course_purchase = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="purchase_course")
    created_at = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user_purchase', 'course_purchase']


class StripeCustomer(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    user_strip_customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="strip_customer_user", unique=True)
    stripe_customer_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)