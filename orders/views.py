from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from excursions.models import Excursion

@login_required
def my_orders(request):
    # Получаем все заказы текущего пользователя
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my_orders.html', {'orders': orders})


@login_required
def order_create(request, excursion_id):
    excursion = get_object_or_404(Excursion, id=excursion_id)

    if request.method == 'POST':
        # Получаем имя и email из формы
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Создаем заказ
        order = Order.objects.create(
            excursion=excursion,
            user=request.user,  # Привязываем заказ к текущему пользователю
            price=excursion.price,  # Цена тура
        )

        # Добавляем сообщение для пользователя, чтобы он знал, что заказ был оформлен
        messages.success(request, f'Вы успешно оформили заказ на экскурсию "{excursion.title}".')

        # Перенаправляем пользователя в личный кабинет (например, в мой список заказов)
        return redirect('orders:my_orders')  # Замените на правильный URL для личного кабинета

    return render(request, 'orders/order_form.html', {'excursion': excursion})


@login_required
def cancel_order(request, order_id):
    # Получаем заказ
    order = Order.objects.get(id=order_id)

    # Проверяем, что заказ принадлежит текущему пользователю
    if order.user == request.user:
        order.status = 'canceled'
        order.save()

    return redirect('orders:my_orders')

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/user_orders.html', {'orders': orders})
