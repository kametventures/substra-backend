# Generated by Django 2.1.2 on 2019-02-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substrapp', '0004_auto_20190213_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='file',
        ),
        migrations.AddField(
            model_name='data',
            name='path',
            field=models.FilePathField(blank=True, max_length=500, null=True),
        ),
    ]