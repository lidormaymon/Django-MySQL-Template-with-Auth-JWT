# Generated by Django 4.2.2 on 2023-07-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_category_categoryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]