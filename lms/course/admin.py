from django.contrib import admin

# Register your models here.

from .models import(
    Course,
    Category,
    Attachment,
    Chapter,
    MuxData,
    UserProgress,
    Purchase,
    StripeCustomer
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
    
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
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
        'file',
        "courseInfo",
        'createdAt',
        'updateAt',
        )
    
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(Attachment, AttachmentAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'description',
        "videoFile",
        "position",
        "isPublished",
        "isFree",
        "course_chapter",
        'createdAt',
        'updateAt',
        )
    
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(Chapter, ChapterAdmin)


class MuxDataAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'assetId',
        'playbackId',
        "chapter_mux_data",
        'createdAt',
        'updateAt',
        )
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(MuxData, MuxDataAdmin)


class UserProgressAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'user_user_progress',
        'chapter_user_progress',
        "is_completed",
        'createdAt',
        'updateAt',
        )
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(UserProgress, UserProgressAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'user_purchase',
        'course_purchase',
        'createdAt',
        'updateAt',
        )
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(Purchase, PurchaseAdmin)



class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'user_strip_customer',
        'stripe_customer_id',
        'createdAt',
        'updateAt',
        )
    def createdAt(self, obj):
        return obj.createdAt.strftime('%Y-%m-%d %H:%M:%S')

    def updateAt(self, obj):
        return obj.updateAt.strftime('%Y-%m-%d %H:%M:%S')
    
admin.site.register(StripeCustomer, StripeCustomerAdmin)