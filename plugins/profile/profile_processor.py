from user_management.models import UserDesinations, UserDetails
from firm_management.models import FirmDetails
from authentication.models import Users
from serializers.profile.profileserializer import BasicFirmProfileSerializer, BasicUserProfileSerializer, DesignationSerializer

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.generics import ListAPIView 


class BasicProfileDetails(ListAPIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'firm':
            firm_details = FirmDetails.objects.get(email=user.email)
            profile_serializer = BasicFirmProfileSerializer(firm_details)
        elif user.user_type == 'firm_user':
            user_details = UserDetails.objects.get(email=user.email)
            user_firm = FirmDetails.objects.get(firmname=user.user_firmname)
            profile_serializer = BasicUserProfileSerializer(user_details)
            user_desigantions = UserDesinations.objects.filter(firmname=user_firm)
            designations = DesignationSerializer(user_desigantions,many=True)
        elif user.user_type == 'vendor':
            user_details = UserDetails.objects.get(email=user.email)
            profile_serializer = BasicUserProfileSerializer(user_details)
        return Response({'success':True,
                        'data':profile_serializer.data,
                        'user_type':user.user_type,
                        'designation':designations.data},
                        status=200)