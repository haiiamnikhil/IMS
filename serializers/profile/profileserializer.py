from firm_management.models import FirmDetails
from user_management.models import UserDesinations, UserDetails
from rest_framework import fields,serializers
from authentication.models import Users


class BasicFirmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmDetails
        fields = ['firmname','nnid','email']


class BasicUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['firmname','fullname','email']


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDesinations
        fields = ['designation']