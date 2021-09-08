from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', SignInUser.as_view(),name="signin_user"),
    path('signin/firm/', SignInFirm.as_view(),name="signin_firm")
]