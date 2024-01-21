from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from estoqueapp import views
from .views import authView, home

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('adicionar_produtos/', views.adicionar_produtos, name='adicionar_produtos'),
    path('admin/', admin.site.urls),
    path('signup/', authView, name='authView'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL)