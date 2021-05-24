# Generated by Django 3.2.3 on 2021-05-23 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0004_alter_url_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 12, 41, 55, 313302), editable=False),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(unique=True),
        ),
    ]