# Generated by Django 3.0.5 on 2020-04-28 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20200427_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 18, 43, 10, 717028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 18, 43, 10, 716649, tzinfo=utc)),
        ),
    ]
