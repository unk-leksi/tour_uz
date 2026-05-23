from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'excursion', 'price', 'status', 'created_at', 'updated_at')  # Параметры для отображения в списке
    list_filter = ('status', 'excursion', 'user')  # Фильтрация по статусу, экскурсии и пользователю
    search_fields = ('user__username', 'excursion__title')  # Поиск по имени пользователя и названию экскурсии
    list_editable = ('status',)  # Возможность редактировать статус заказа прямо в списке

    # Дополнительные опции, если нужно
    ordering = ('-created_at',)  # Сортировка по времени создания в убывающем порядке

admin.site.register(Order, OrderAdmin)
