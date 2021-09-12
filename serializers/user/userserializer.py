from user_management.models import UserDetails
from rest_framework import fields, serializers
from authentication.models import Users

class ListUserSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="status.get_status_display",read_only=True)
    register_on = serializers.DateTimeField(format='%d-%m-%Y',read_only=True)
    class Meta:
        model = UserDetails
        fields = ['fullname','email','firmname','status','userid','register_on']