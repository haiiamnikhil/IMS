# Generated by Django 3.1 on 2021-09-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_auto_20210908_1339'),
        ('firm_management', '0006_delete_historicalfirms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firmstatus',
            name='firmname',
        ),
        migrations.RemoveField(
            model_name='historicalfirmstatus',
            name='firmname',
        ),
        migrations.RemoveField(
            model_name='historicalfirmstatus',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='Firms',
        ),
        migrations.DeleteModel(
            name='FirmStatus',
        ),
        migrations.DeleteModel(
            name='HistoricalFirmStatus',
        ),
    ]
