# Generated by Django 3.1 on 2021-09-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210908_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalusers',
            name='user_type',
            field=models.CharField(choices=[('Firm', 'firm'), ('Admin', 'admin'), ('Firm Client', 'firm client'), ('Vendor', 'vendor')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('Firm', 'firm'), ('Admin', 'admin'), ('Firm Client', 'firm client'), ('Vendor', 'vendor')], max_length=50, null=True),
        ),
    ]
