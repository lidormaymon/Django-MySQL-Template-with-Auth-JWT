# Generated by Django 4.2.2 on 2023-06-29 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='createdTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
