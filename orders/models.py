from django.db import models
from django.conf import settings
from excursions.models import Excursion  # импорт модели Экскурсия

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Связь с пользователем
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, related_name='orders')  # Связь с экскурсией
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена экскурсии
    status = models.CharField(max_length=50, choices=[  # Статус заказа
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled')
    ], default='pending')

    def __str__(self):
        return f'Order {self.id} - {self.excursion.title} - {self.status}'

    class Meta:
        ordering = ['-created_at']

