# Generated by Django 2.2.17 on 2021-04-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='contact_receipt',
            field=models.BooleanField(default=False, verbose_name='계약서 수취'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='joined_date',
            field=models.DateField(auto_now_add=True, verbose_name='계약일'),
        ),
    ]