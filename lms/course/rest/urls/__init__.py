from django.urls import include, path


urlpatterns = [ 
    path("", include("course.rest.urls.course")),
    path("category/", include("course.rest.urls.category"))
]