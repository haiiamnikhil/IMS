from django.urls import path
from plugins.firm.firm_processor import ListFirms

urlpatterns = [
    path('',ListFirms.as_view(),name='list_firms')
]