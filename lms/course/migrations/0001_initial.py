# Generated by Django 4.2.7 on 2023-11-13 11:37

import course.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_index=True, max_length=100, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                (
                    "userId",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("title", models.CharField(db_index=True, max_length=500)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "imageUrl",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to=course.utils.get_course_image
                    ),
                ),
                ("price", models.FloatField(blank=True, default=0, null=True)),
                ("isPublished", models.BooleanField(default=False)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updateAt", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseCollectionBridge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.category",
                    ),
                ),
                (
                    "courses",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
            options={
                "unique_together": {("courses", "category")},
                "index_together": {("category", "category")},
            },
        ),
        migrations.AddField(
            model_name="course",
            name="categories",
            field=models.ManyToManyField(
                through="course.CourseCollectionBridge", to="course.category"
            ),
        ),
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_index=True, max_length=200, null=True
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updateAt", models.DateTimeField(auto_now=True)),
                (
                    "courseInfo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
        ),
    ]
