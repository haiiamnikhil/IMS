# Generated by Django 3.1 on 2021-09-06 09:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firm_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirmStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=2, max_length=50, null=True)),
                ('updated_on', models.DateField(default=datetime.date(2021, 9, 6))),
                ('firmname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firmstatus_firm_name', to='firm_management.firms')),
            ],
            options={
                'verbose_name_plural': 'Firm Status',
            },
        ),
        migrations.RenameModel(
            old_name='HistoricalFirmInfo',
            new_name='HistoricalFirmStatus',
        ),
        migrations.AlterModelOptions(
            name='historicalfirmstatus',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical firm status'},
        ),
        migrations.DeleteModel(
            name='FirmInfo',
        ),
    ]