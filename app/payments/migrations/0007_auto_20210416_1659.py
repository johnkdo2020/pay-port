# Generated by Django 2.2.17 on 2021-04-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20210416_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default='PAYGO165958454715', max_length=25, verbose_name='주문번호'),
        ),
    ]