from firm_management.models import FirmsList
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
from plugins.user.user_processor import UserValidator


@method_decorator(csrf_exempt,name="dispatch")
class SignUpUser(View):
    def __init__(self):
        self.template_name = 'auth/register.html'
        self.auth = UserValidator()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        auth = self.auth.verify_user(request)
        if auth['status']:
            return JsonResponse({'success':True},status=200,safe=False)
        else:
            return JsonResponse({'success':False,'message':auth['message']},status=200,safe=False)