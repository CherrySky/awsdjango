# Generated by Django 2.1.2 on 2018-12-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_auto_20181203_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='receipt_pic',
            field=models.ImageField(blank=True, upload_to='upload_receipt'),
        ),
    ]
