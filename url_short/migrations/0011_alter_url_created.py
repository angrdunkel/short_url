# Generated by Django 3.2.3 on 2021-05-23 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0010_auto_20210523_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 13, 30, 25, 746688), editable=False),
        ),
    ]