from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Excursion

@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'duration', 'image_preview')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    ordering = ('date',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="60" style="object-fit:cover;" />')
        return "-"
    image_preview.short_description = 'Изображение'