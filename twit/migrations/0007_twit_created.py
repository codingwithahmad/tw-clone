# Generated by Django 3.2.7 on 2021-10-02 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0006_alter_twit_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 10, 45, 41, 959156, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]