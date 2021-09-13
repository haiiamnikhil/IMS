from django.urls import path
from user_management.views import user_signup, list_users

urlpatterns = [
    path('signup/user/',user_signup.SignUpUser.as_view(),name="signup_user"),
    path('user/list-user/',list_users.ListUsers.as_view(),name="list_users"),
]