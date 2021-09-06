from django.urls import path
from .views import *

urlpatterns = [
    path('signin/user/', SignInUser.as_view(),name="signin_user"),
    path('signup/', SignUpUser.as_view(),name="signup"),
    path('signin/firm/', SignInFirm.as_view(),name="signin_firm")
]