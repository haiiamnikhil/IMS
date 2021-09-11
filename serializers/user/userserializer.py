from rest_framework import fields, serializers
from authentication.models import Users

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['fullname','email','designation','']