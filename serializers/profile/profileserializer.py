from rest_framework import fields,serializers
from authentication.models import Users


class BasicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email','firmname','nnid','user_type']