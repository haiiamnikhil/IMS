from django.urls import path,include

urlpatterns = [
    path('',include('app.urls')),
    path('profile/',include('app.url_plugins'))
]