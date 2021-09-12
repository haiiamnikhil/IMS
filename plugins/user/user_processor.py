from authentication.models import Users
from rest_framework.parsers import JSONParser
from plugins.config import status_configure
from django.contrib.auth.hashers import make_password

class UserValidator():
    def __init__(self):
        self.parser = JSONParser()
        self.status = status_configure()

    def verify_user(self, request):
        data = self.parser.parse(request)
        user = Users.objects.filter(email=data['email'],user_firmname=data['user_firmname']).exists()
        print(user)
        if user:
            self.status['status'] = False
            self.status['message'] = f"User Already registered with {data['user_firmname']}"
            return self.status 
        else:
            data['password'] = make_password(data['password'])
            Users.objects.create(**data)
            self.status['status'] = True
            return self.status