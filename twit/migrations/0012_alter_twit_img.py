# Generated by Django 3.2.7 on 2021-10-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0011_alter_twit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
