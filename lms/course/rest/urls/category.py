from django.urls import path

from ..views import category


urlpatterns = [
    path('', 
         category.CategoryList.as_view(),
         name='category-list-create'),

    path("<uuid:uid>/", 
         category.CategoryDetails.as_view(),
         name="category-update-delete"),
]