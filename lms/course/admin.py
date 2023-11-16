from django.contrib import admin

# Register your models here.

from .models import(
    Course,
    Category,
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'name'
        )
    
admin.site.register(Category, CategoryAdmin)