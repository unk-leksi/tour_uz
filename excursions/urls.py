# excursions/urls.py
from django.urls import path
from . import views

app_name = 'excursions'  # Убедитесь, что указали имя приложения

urlpatterns = [
    path('', views.excursion_list, name='excursion_list'),  # маршрут для списка экскурсий
    path('<int:excursion_id>/', views.excursion_detail, name='excursion_detail'),
    path('create/', views.excursion_create, name='excursion_create'),
    path('<int:excursion_id>/edit/', views.excursion_edit, name='excursion_edit'),
]
