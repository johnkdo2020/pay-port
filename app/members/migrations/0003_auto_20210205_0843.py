# Generated by Django 2.2.17 on 2021-02-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0005_auto_20210203_0934'),
        ('members', '0002_connectpaygousermanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paygouser',
            name='paygocomputationalmanagers',
        ),
        migrations.AddField(
            model_name='paygouser',
            name='pay_managers',
            field=models.ManyToManyField(blank=True, help_text='전산 관리자', through='members.ConnectPayGoUserManager', to='owners.PayGoComputationalManager'),
        ),
    ]
