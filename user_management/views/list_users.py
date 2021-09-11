from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from authentication.models import Users
from serializers.profile.profileserializer import BasicProfileSerializer
from rest_framework.generics import CreateAPIView

from authentication.models import Users

class ListUsers(CreateAPIView):
    renderer_classes = [JSONRenderer,TemplateHTMLRenderer]
    template_name = 'user/listusers.html'

    def get(self, request, *args, **kwargs):
        user_details = Users.objects.get(email=request.user.email)
        user_list = self.get_user_list(request)
        profile_serializer = BasicProfileSerializer(user_details)
        return Response({'success':True,'data':profile_serializer.data},status=200)

    def get_user_list(self, request):
        user = request.user
        list_user = Users.objects.filter(firmname=user.firmname, user_type='firm_client')
        
