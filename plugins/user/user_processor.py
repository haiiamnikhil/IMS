from authentication.models import Users
from rest_framework.parsers import JSONParser
from plugins.config import status_configure

class UserValidator():
    def __init__(self):
        self.parser = JSONParser()
        self.status = status_configure()

    def verify_user(self, request):
        data = self.parser.parse(request)
        print(data)
        try:
            Users.objects.get(email=data['email'])
        except Users.DoesNotExist:
            Users.objects.create(**data)
            self.status['status'] = True
            print("success")
            return self.status
        except Exception as e:
            print(e)
            self.status['status'] = False
            self.status['message'] = "Account Alredy Exists"
            print(self.status)
            return self.status
        # if user.exists():
        # else:
          