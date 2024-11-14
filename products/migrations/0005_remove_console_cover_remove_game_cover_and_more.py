# Generated by Django 4.2.16 on 2024-11-14 08:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_console_product_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='console',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='game',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='cover',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='console',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.console'),
        ),
        migrations.AlterField(
            model_name='product',
            name='game',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.game'),
        ),
    ]