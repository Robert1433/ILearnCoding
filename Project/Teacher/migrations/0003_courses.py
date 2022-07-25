# Generated by Django 4.0.5 on 2022-07-12 12:07

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_delete_message_room_slug_alter_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('prof_user', models.CharField(max_length=255, null=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('file', models.FileField(null=True, upload_to='files')),
                ('imag', models.ImageField(null=True, upload_to='imag')),
                ('creation_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
    ]
