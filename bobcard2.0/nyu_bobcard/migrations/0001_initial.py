# Generated by Django 2.1.3 on 2018-12-06 12:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ManyToManyField(to='nyu_bobcard.Location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('entry_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('requested_time', models.DateTimeField()),
                ('requested_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nyu_bobcard.Location')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyu_bobcard.Student')),
            ],
            options={
                'ordering': ['entry_time'],
            },
        ),
    ]
