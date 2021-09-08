from authentication.models import Users

class VerifyUser:
    def get_user_type(self,email):
        user = Users.objects.get(email=email)
        user_type = user.user_type
        return user_type