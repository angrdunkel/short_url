# Generated by Django 3.2.3 on 2021-05-23 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0005_auto_20210523_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created',
            field=models.DateTimeField(default=datetime.date.today, editable=False),
        ),
    ]
