from django.urls import path,include

urlpatterns = [
    path('signup/',include('firm_management.urls'))
]