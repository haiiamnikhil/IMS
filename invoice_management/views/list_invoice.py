from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.generics import ListCreateAPIView

class ListInvoice(ListCreateAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'invoice/list-invoice.html'

    def get(self, request, *args, **kwargs):
        return Response({'success':True},status=200)