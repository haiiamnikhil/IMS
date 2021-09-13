from django.urls import path
from invoice_management.views.list_invoice import ListInvoice


urlpatterns = [
    path('list-invoice/',ListInvoice.as_view(),name='list-invoice')
]