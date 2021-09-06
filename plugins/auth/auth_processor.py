from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from user_management.models import UserStatus
from firm_management.models import FirmStatus
from plugins.config import status_configure

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
            account_status = UserStatus.objects.get(user=user)
            if account_status.status == 1:
                self.status['status'] = True
                return self.status
            else:
                self.status['status'] = False
                self.status['message'] = f"Your Account is under {account_status.get_status_display()}"
                return self.status
        else:
            return self.status.get('status',False)

    def signup_auth(self,request):
        user_data = self.parser.parse(request)
        print(user_data)
        return True

    def firm_auth(self,request):
        self.data = self.parser.parse(request)
        firm = authenticate(request,username=self.data['username'],password=self.data['password'])
        if firm is not None:
            firm_status = FirmStatus.objects.get(firmname=firm)
            if firm_status.status == 1:
                self.status['status'] = True
                return self.status
            else:
                self.status['status'] = False
                self.status['message'] = f"Your Account is under {firm_status.get_status_display()}"
                return self.status
        else:
            self.status['status'] = False
            self.status['message'] = "Entered Credentials don't match'"
            return self.status

        