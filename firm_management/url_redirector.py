from django.urls import path,include

urlpatterns = [
    path('signup/',include('firm_management.urls')),
    path('listfirms/',include('firm_management.url_plugins'))
]