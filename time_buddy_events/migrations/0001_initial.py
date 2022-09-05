# Generated by Django 4.1 on 2022-08-31 01:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=250, verbose_name='location')),
                ('summary', models.CharField(max_length=50, verbose_name='summary')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'events',
                'ordering': ['event_id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Time_Zone',
            fields=[
                ('tz_id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='tz_id')),
                ('tz_name', models.CharField(max_length=50, verbose_name='tz_name')),
            ],
            options={
                'verbose_name': 'Time_Zone',
                'verbose_name_plural': 'Time_Zones',
                'db_table': 'time_zones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Event_Instance',
            fields=[
                ('instance_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='insance_id')),
                ('dt_start', models.DateTimeField(verbose_name='dt_start')),
                ('dt_end', models.DateTimeField(verbose_name='dt_end')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_buddy_events.event')),
            ],
            options={
                'verbose_name': 'Event Instance',
                'verbose_name_plural': 'Event Instances',
                'db_table': 'event_instances',
                'ordering': ['instance_id'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_buddy_events.time_zone'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_buddy_events.user'),
        ),
    ]
