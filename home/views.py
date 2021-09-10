from django.shortcuts import render
from django.views import View


class Dashboard(View):
    def __init__(self):
        self.template_name = 'app/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)