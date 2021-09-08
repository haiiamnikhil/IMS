# Generated by Django 3.1 on 2021-09-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210908_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalusers',
            name='user_type',
            field=models.CharField(choices=[('firm', 'Firm'), ('admin', 'Admin'), ('firm_client', 'Firm Client'), ('vendor', 'Vendor')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('firm', 'Firm'), ('admin', 'Admin'), ('firm_client', 'Firm Client'), ('vendor', 'Vendor')], max_length=50, null=True),
        ),
    ]
