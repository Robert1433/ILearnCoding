# Generated by Django 4.0.5 on 2022-07-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='utype',
            field=models.TextField(blank=True, null=True),
        ),
    ]
