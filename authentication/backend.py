from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from firm_management.models import Firms
from django.contrib.auth.hashers import check_password

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

class FirmAuth(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        try:
            firm = Firms.objects.get(firm_email=username)
        except Firms.DoesNotExist:
            return None
        
        if check_password(password,firm.password) and self.user_can_authenticate(firm):
            return firm
        else:
            return None