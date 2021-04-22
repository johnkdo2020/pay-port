# Generated by Django 2.2.17 on 2021-04-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymethod', '0004_auto_20210316_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlementinformation',
            name='agency_fee',
            field=models.FloatField(default=0.1, verbose_name='에이전트 수수료'),
        ),
        migrations.AddField(
            model_name='settlementinformation',
            name='paygo_fee',
            field=models.FloatField(default=3.1, verbose_name='페이고 수수료'),
        ),
    ]