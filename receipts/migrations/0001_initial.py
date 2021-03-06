# Generated by Django 2.1.2 on 2018-12-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('purchase_date', models.DateTimeField()),
                ('expired_date', models.DateTimeField()),
                ('maintenance_period', models.DecimalField(decimal_places=1, max_digits=10)),
                ('shop_name', models.CharField(max_length=200)),
                ('shop_phone', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=200)),
                ('invoice_number', models.CharField(max_length=200)),
            ],
        ),
    ]
