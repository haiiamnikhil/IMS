from django.urls import path
from .views import *


urlpatterns = [
    path('register-firm/', RegisterFirm.as_view(),name='register_firm'),
]