# Generated by Django 4.1.4 on 2023-10-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_orderitemsmodel_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]
