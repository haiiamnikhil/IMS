from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login

from plugins.auth.auth_processor import *
from plugins.firm.firm_processor import *


@method_decorator(csrf_exempt,name="dispatch")
class SignInUser(View):
    def __init__(self):
        self.template_name = 'auth/login.html'
        self.auth = AuthProcessor()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        auth = self.auth.signin_auth(request)
        print(auth)
        if auth['status']:
            login(request, auth['user'])
            return JsonResponse({'success': True},safe=False,status=200)
        else:
            return JsonResponse({'success': False},safe=False,status=200)


@method_decorator(csrf_exempt,name="dispatch")
class SignInFirm(View):
    def __init__(self):
        self.template_name = 'auth/login.html'
        self.auth = AuthProcessor()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth = self.auth.firm_auth(request)
        if auth['status']:
            login(request,auth['user'])
            
            return JsonResponse({'success': True},status=200,safe=False)
        else:
            return JsonResponse({'success': False,'message':auth['message']},status=200,safe=False)