from django.contrib import admin

# Register your models here.

from .models import(
    Course
)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'userId',
        'title',
        'description',
        "imageUrl",
        "price",
        "isPublished",
        'createdAt',
        'updateAt',
        )
    
admin.site.register(Course, CourseAdmin)