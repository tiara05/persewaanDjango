# Generated by Django 3.0.5 on 2020-04-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
