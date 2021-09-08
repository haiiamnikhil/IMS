# Generated by Django 3.1 on 2021-09-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210908_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalusers',
            name='firmname',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='firmname',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
