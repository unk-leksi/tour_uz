# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Order
#
# @receiver(post_save, sender=Order)
# def notify_admin_about_new_order(sender, instance, created, **kwargs):
#     if created:
#         # Отправка письма администратору
#         send_mail(
#             'Новый заказ на экскурсию',
#             f'Пользователь {instance.user.username} оформил заказ на экскурсию "{instance.excursion.title}".',
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.ADMIN_EMAIL],  # Email администратора
#         )
