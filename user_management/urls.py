from django.urls import path
from .views import *

urlpatterns = [
    path('user/',SignUpUser.as_view(),name="signup_user")
]