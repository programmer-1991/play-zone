# Generated by Django 4.2.16 on 2024-11-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]