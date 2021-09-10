from user_management.models import UserOnboardingTracker
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect


class GetStartedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.onboard_level = UserOnboardingTracker.ONBOARDING_LEVELS[:-1]
        self.redirects = {
            '0':'get_started',
        }
        self.user_details = '/profile/details/'

    def __call__(self, request):
        user = request.user
        if request.method == 'GET':
            if user.is_authenticated and user.is_superuser:
                pass
            elif user.is_authenticated:
                user_onboard = UserOnboardingTracker.objects.get(user=user)
                user_status = user_onboard.status
                for status in self.onboard_level:
                    if user_status in status:
                        if not request.path == reverse(self.redirects[user_status]) and request.path != self.user_details:
                            return HttpResponseRedirect(reverse(self.redirects[user_status]))
                        pass
                    else:
                        pass
            else:pass
        elif request.method == 'POST':
            pass
        response = self.get_response(request)
        return response