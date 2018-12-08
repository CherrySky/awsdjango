from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Receipt
from django.conf import settings


class ReceiptAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['brand_name', 'product_name']}),
    #     ('Date information', {'fields': ['purchase_date', 'expired_date'], 'classes': ['collapse']}),
    # ]
    list_filter = ['purchase_date', 'brand_name']
    search_fields = ['product_name', 'brand_name']
    list_display = ('product_name', 'brand_name', 'price', 'expired_date', 'was_expired')
    readonly_fields = ['display_photo']

    def display_photo(self, obj):
        if obj.receipt_pic and obj.id:
            return mark_safe('<img src="{url}" height={height} width={width} />'.format(
                url=obj.receipt_pic.url,
                height=obj.receipt_pic.height,
                width=obj.receipt_pic.width
            ))
        else:
            return ''
    display_photo.short_description = 'ReceiptImage'
    display_photo.allow_tags = True


admin.site.register(Receipt, ReceiptAdmin)