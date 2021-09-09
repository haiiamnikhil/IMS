from django.urls import path
from plugins.profile.profile_processor import BasicProfileDetails

urlpatterns = [
    path('details/',BasicProfileDetails.as_view(),name="basic_profile")
]