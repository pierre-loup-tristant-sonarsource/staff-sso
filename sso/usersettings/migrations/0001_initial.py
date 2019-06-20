# Generated by Django 2.1.7 on 2019-05-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, verbose_name='unique user id')),
                ('app_slug', models.CharField(blank=True, max_length=50, verbose_name='app slug')),
                ('settings', models.TextField(verbose_name='settings')),
            ],
        ),
    ]