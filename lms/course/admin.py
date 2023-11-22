from django.contrib import admin

# Register your models here.

from .models import(
    Course,
    Category,
    Attachment
)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'userId',
        'title',
        'description',
        "imageUrl",
        "price",
        "categories",
        "isPublished",
        'createdAt',
        'updateAt',
        )
    
admin.site.register(Course, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'name'
        )
    
admin.site.register(Category, CategoryAdmin)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'name',
        'url',
        "courseInfo",
        'createdAt',
        'updateAt',
        )
admin.site.register(Attachment, AttachmentAdmin)