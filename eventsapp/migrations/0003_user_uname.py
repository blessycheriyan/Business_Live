# Generated by Django 3.1.5 on 2021-01-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0002_auto_20210118_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uname',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
