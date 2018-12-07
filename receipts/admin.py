from django.contrib import admin

from .models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['brand_name', 'product_name']}),
    #     ('Date information', {'fields': ['purchase_date', 'expired_date'], 'classes': ['collapse']}),
    # ]
    list_filter = ['purchase_date', 'brand_name']
    search_fields = ['product_name', 'brand_name']
    list_display = ('product_name', 'brand_name', 'price', 'expired_date', 'was_expired')


admin.site.register(Receipt, ReceiptAdmin)
