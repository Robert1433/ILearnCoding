# Generated by Django 4.0.5 on 2022-07-15 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0007_delete_quesmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]