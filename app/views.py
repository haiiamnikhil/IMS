from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from firm_management.models import FirmDetails
from user_management.models import UserDetails
from rest_framework.parsers import JSONParser
from user_management.models import UserOnboardingTracker


@method_decorator(csrf_exempt,name="dispatch")
class GetStarted(View):
    def __init__(self):
        self.template_name = 'app/getstarted.html'
        self.parser = JSONParser()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = self.parser.parse(request)
        if user.user_type == 'firm':
            firm = FirmDetails.objects.create(**data)
            if firm is not None:
                user = UserOnboardingTracker.objects.get(user=user)
                user.status = '1'
                user.save()
                return JsonResponse({'success':True},safe=False,status=200)
            else:
                pass
        elif user.user_type == 'firm_user':
            client = UserDetails.objects.create(**data)
            if client is not None:
                user = UserOnboardingTracker.objects.get(user=user)
                user.status = '1'
                user.save()
                return JsonResponse({'success':True},safe=False,status=200)
            else:pass
        else:
            return JsonResponse({'success':False},safe=False,status=200)