from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class GetStarted(View):
    def __init__(self):
        self.template_name = 'app/getstarted.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return JsonResponse({'success':True},safe=False,status=200)