# Generated by Django 3.1 on 2021-09-11 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_management', '0004_auto_20210909_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmname', models.CharField(blank=True, max_length=150, null=True)),
                ('fullname', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('userid', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('join_date', models.DateField(null=True)),
                ('register_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Details',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUserDetails',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('firmname', models.CharField(blank=True, max_length=150, null=True)),
                ('fullname', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('userid', models.CharField(blank=True, db_index=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('join_date', models.DateField(null=True)),
                ('register_on', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user details',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]