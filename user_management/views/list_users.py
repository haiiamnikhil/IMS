from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from authentication.models import Users
from user_management.models import UserDetails
from serializers.user.userserializer import ListUserSerializer
from rest_framework.generics import CreateAPIView

from authentication.models import Users

class ListUsers(CreateAPIView):
    renderer_classes = [JSONRenderer,TemplateHTMLRenderer]
    template_name = 'user/listusers.html'

    def get(self, request, *args, **kwargs):
        user_list = self.get_user_list(request)
        print(user_list)
        list_user = ListUserSerializer(user_list,many=True)
        return Response({'success':True,'data':list_user.data},status=200)

    def get_user_list(self, request):
        user = request.user
        print(user.firmname)
        list_user = UserDetails.objects.filter(firmname=user.firmname)
        return list_user
        
