from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', SignInUser.as_view(),name="signin_user"),
    path('signout/', signOut,name="signout_user")
]