# Generated by Django 2.2 on 2020-06-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_register_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carvehicle',
            name='owned_by',
            field=models.EmailField(max_length=254),
        ),
    ]
