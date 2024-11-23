# Generated by Django 4.2.16 on 2024-11-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('topic', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=254, null=True)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
