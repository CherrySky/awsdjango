import datetime
from django.db import models
from django.utils import timezone


# Create your models here.


class Receipt(models.Model):
    brand_name = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=1, max_digits=10)
    purchase_date = models.DateTimeField()
    expired_date = models.DateTimeField()
    maintenance_period = models.DecimalField(decimal_places=1, max_digits=10)
    shop_name = models.CharField(max_length=200, blank=True)
    shop_phone = models.CharField(max_length=20, blank=True)
    shop_address = models.CharField(max_length=200, blank=True)
    invoice_number = models.CharField(max_length=200, blank=True)
    serial_number = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=200, blank=True)

    # receipt_file = models.FileField()

    def __str__(self):
        return self.product_name

    def was_expired(self):
        now = timezone.now()
        return now <= self.expired_date

    was_expired.admin_order_field = 'expired_date'
    was_expired.boolean = True
    was_expired.short_description = 'Having Maintenance?'
