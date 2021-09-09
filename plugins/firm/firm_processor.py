from rest_framework.parsers import JSONParser
from authentication.models import Users
from django.contrib.auth.hashers import make_password
from plugins.config import status_configure
from serializers.firm.firmserializer import FirmsListSerializer
from firm_management.models import FirmsList
from django.http import JsonResponse
from django.views import View


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
        
        try:
            Users.objects.get(email=data['email'])
        except Users.DoesNotExist:
            Users.objects.create(**data)
            self.status['status'] = True
            return self.status
        
        self.status['status'] = False
        self.status['message'] = "Account alredy exists"
        return self.status
            

class ListFirms(View):
    def get(self,request):
        list_firms = FirmsList.objects.all()
        firms_list_serializer = FirmsListSerializer(list_firms,many=True)
        return JsonResponse({'success':True,'data':firms_list_serializer.data},safe=False,status=200)