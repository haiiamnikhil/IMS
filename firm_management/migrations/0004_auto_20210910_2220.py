# Generated by Django 3.1 on 2021-09-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm_management', '0003_auto_20210910_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmdetails',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='historicalfirmdetails',
            name='email',
            field=models.EmailField(db_index=True, max_length=50, null=True),
        ),
    ]
