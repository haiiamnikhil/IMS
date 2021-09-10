from django.http import JsonResponse
from django.views import View
from authentication.models import Users
from serializers.profile.profileserializer import BasicProfileSerializer
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt,name="dispatch")
class BasicProfileDetails(View):
    def __init__(self):
        self.parser = JSONParser()

    def get(self, request, *args, **kwargs):
        user = request.user
        user_details = Users.objects.get(email=user.email)
        profile_serializer = BasicProfileSerializer(user_details)
        return JsonResponse({'success':True,'data':profile_serializer.data},status=200,safe=False)