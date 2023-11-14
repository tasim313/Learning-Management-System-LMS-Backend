from django.urls import path

from ..views import course


urlpatterns = [
    path('', 
         course.CourseList.as_view(),
         name='course-list-create'),

    path("<uuid:uid>/", 
         course.CourseDetails.as_view(),
         name="course-update-delete"),
]