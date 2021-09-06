from rest_framework.parsers import JSONParser
from firm_management.models import Firms
from django.contrib.auth.hashers import make_password
from plugins.config import status_configure

class FirmValidator():
    def __init__(self):
        self.parser = JSONParser()
        self.status = status_configure()

    def firm_details(self, request):
        data = self.parser.parse(request)
        # if FirmDetails.objects.filter()
        return True

    def verify_firm(self, request):
        data = self.parser.parse(request)
        data['password'] = make_password(data['password'])
        print(data)
        firm = Firms.objects.filter(firmname=data['firmname'])
        if firm.exists():
            self.status['status'] = False
            self.status['message'] = "Account alredy exists"
            return self.status
        else:
            Firms.objects.create(**data)
            self.status['status'] = True
            return self.status