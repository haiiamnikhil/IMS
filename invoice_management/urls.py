from django.urls import path,include

urlpatterns = [
    path('invoice/', include('invoice_management.url_views'))
]
