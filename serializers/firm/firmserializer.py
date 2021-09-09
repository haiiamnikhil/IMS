from rest_framework import fields, serializers
from firm_management.models import FirmsList


class FirmsListSerializer(serializers.ModelSerializer):
    firmname = serializers.CharField(source='firmname.firmname',read_only=True)
    class Meta:
        model = FirmsList
        fields = ['firmname']