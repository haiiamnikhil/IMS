from django.urls import path
from .views import *


urlpatterns = [
    path('firm/', RegisterFirm.as_view(),name='register_firm'),
]