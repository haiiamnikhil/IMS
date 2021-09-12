from django.contrib import admin
from .models import *

admin.site.register(UserInvites)
admin.site.register(UserStatus)
admin.site.register(UserOnboardingTracker)
admin.site.register(UserDetails)