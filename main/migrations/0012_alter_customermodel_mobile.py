# Generated by Django 4.1.4 on 2023-10-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_vendor_isverified_vendor_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='mobile',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
