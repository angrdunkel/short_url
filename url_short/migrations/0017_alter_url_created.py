# Generated by Django 3.2.3 on 2021-05-23 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0016_alter_url_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 14, 38, 28, 794296), editable=False),
        ),
    ]
