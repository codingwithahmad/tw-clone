# Generated by Django 3.2.7 on 2021-10-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='media/images/default.jpg', upload_to='images/profile_photo', verbose_name='عکس پروفایل'),
        ),
    ]
