# Generated by Django 2.2.17 on 2021-04-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20210415_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default='PAYGO165016799423', max_length=25, verbose_name='주문번호'),
        ),
    ]