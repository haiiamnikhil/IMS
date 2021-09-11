from django.shortcuts import redirect
from django.urls import reverse


class BaseRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == 'GET':
            path = request.path
            user = request.user
            if path == '/' and user.is_authenticated:
                return redirect(reverse('dashboard'))
            # elif not user.is_authenticated and not request.path == reverse('signin_user'):
            elif not user.is_authenticated and not request.path == reverse('signin_user'):
                return redirect(reverse('signin_user'))
            else:pass

        response = self.get_response(request)

        return response