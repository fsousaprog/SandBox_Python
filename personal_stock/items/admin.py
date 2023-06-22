from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "avg_price")


# Register your models here.
admin.site.register(Item, ItemAdmin)
