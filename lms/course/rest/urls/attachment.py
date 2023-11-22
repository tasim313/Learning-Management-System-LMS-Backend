from django.urls import path

from ..views import attachment


urlpatterns = [
    path('', 
         attachment.AttachmentList.as_view(),
         name='attachment-list-create'),

    path("<uuid:uid>/", 
         attachment.AttachmentDetails.as_view(),
         name="attachment-update-delete"),
]