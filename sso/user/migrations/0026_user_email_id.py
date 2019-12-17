# Generated by Django 2.2.4 on 2019-12-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20191014_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_user_id',
            field=models.EmailField(default='', help_text='An user id an email compatible format', max_length=254),
            preserve_default=False,
        ),
    ]
