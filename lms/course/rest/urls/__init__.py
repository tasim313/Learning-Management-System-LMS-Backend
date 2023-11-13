from django.urls import include, path


urlpatterns = [ 
    path("", include("course.rest.urls.course")),
]