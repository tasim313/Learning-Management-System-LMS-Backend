# Generated by Django 4.2.7 on 2023-11-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_alter_course_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
