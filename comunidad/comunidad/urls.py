from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagos.urls')),
    path('', LoginView.as_view()),
    
]
admin.site.site_header = 'SYS Comunidad, sistema de control de pagos Socios'
