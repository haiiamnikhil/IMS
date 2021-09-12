from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from user_management.models import UserStatus, UserOnboardingTracker
from plugins.config import status_configure
from .auth_user_type import VerifyUser

class AuthProcessor():

    def __init__(self):
        self.data = {}
        self.parser = JSONParser()
        self.status = status_configure()

    def signin_auth(self,request):        
        self.data.update({"username": request.POST.get('username'), 
                    "password" : request.POST.get('password')})
        user = authenticate(request,username=self.data['username'],password=self.data['password'])
        if user:
            user_type = VerifyUser().get_user_type(self.data['username'])
            onboard_status = UserOnboardingTracker.objects.get(user=user)
            account_status = UserStatus.objects.get(user=user)
            print(account_status)
            if int(account_status.status) == 1:
                self.status['status'] = True
                self.status['user'] = user
                self.status['onboard_status'] = onboard_status.status
                return self.status
            else:
                self.status['status'] = False
                self.status['message'] = f"Your Account is under {account_status.get_status_display()}"
                return self.status
        else:
            self.status['status'] = False
            self.status['message'] = f"Entered Credentials is Incorrect"
            return self.status

