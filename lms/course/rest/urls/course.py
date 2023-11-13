from django.urls import path

from ..views import course


urlpatterns = [
    path('', 
         course.CourseList.as_view(),
         name='course-list-create'),
]