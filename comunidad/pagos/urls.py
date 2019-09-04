from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('cuotas/',views.listacuotas, name='cuotas'),
    url('perfil/', views.perfil, name="perfil"),
    url('pagos', views.pagos_new, name='pagos_new'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^',views.pagina_inicio, name='pagina_inicio'),
] 