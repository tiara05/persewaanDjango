# Generated by Django 3.0.5 on 2020-04-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_product_product_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
