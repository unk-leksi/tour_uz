from django.contrib import admin
from django.urls import path, include
from tour_uz import views
from django.contrib.auth import views as auth_views
from .views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # Это подключает стандартные URL для авторизации и регистрации
    path('excursions/', include('excursions.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),  # Это маршрут для главной страницы
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
