from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from plugins.firm.firm_processor import FirmValidator


@method_decorator(csrf_exempt, name="dispatch")
class RegisterFirm(View):
    def __init__(self):
        self.template_name = 'firm/register_firm.html'
        self.firm = FirmValidator()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        status = self.firm.verify_firm(request)
        if status['status']:
            return JsonResponse({'success':True},safe=False,status=200)
        else:
            return JsonResponse({'success':False},safe=False,status=200)