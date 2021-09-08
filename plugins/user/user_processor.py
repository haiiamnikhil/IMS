from authentication.models import Users
from rest_framework.parsers import JSONParser
from plugins.config import status_configure

class UserValidator():
    def __init__(self):
        self.parser = JSONParser()
        self.status = status_configure()

    def verify_username(self, request):
        data = self.parser.parse(request)
        user = Users.objects.get(email=data['email'])
        if user is None:
            self.status['status'] = True
            print(data)
            return self.status
        else:
            self.status['status'] = False
            self.status['message'] = "Account Alredy Exists"
            return self.status  

class ListFirms:
    def get_firms(self):
        pass