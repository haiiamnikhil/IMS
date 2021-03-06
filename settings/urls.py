from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/',include('authentication.urls')),
    path('',include('firm_management.url_redirector')),
    path('',include('user_management.urls')),

    path('',include('app.url_redirector')),
    path('home/',include('home.url_redirector')),
    path('',include('invoice_management.urls'))
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)