# Generated by Django 3.2.7 on 2021-09-29 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0004_twit_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twit',
            name='bio',
        ),
    ]
