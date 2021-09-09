from django.http import JsonResponse
from django.views import View
from authentication.models import Users
from serializers.profile.profileserializer import BasicProfileSerializer


class BasicProfileDetails(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_details = Users.objects.get(email=user.email)
        profile_serializer = BasicProfileSerializer(user_details)
        print(profile_serializer.data)
        return JsonResponse({'success':True,'data':profile_serializer.data},status=200,safe=False)
    