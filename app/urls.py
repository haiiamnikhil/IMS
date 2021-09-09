from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('getstarted/',GetStarted.as_view(),name="get_started"),
]
