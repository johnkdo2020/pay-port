# Generated by Django 2.2.17 on 2021-04-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20210423_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default='PAYGO133101200425', max_length=25, unique=True, verbose_name='주문번호'),
        ),
    ]