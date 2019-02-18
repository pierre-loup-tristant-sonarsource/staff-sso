# Generated by Django 2.0.8 on 2018-11-01 15:52

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    User = apps.get_model('user', 'User')
    for user in User.objects.all():
        user.user_id = uuid.uuid4()
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user_last_accessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, unique=False, verbose_name='unique user id'),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(unique=True)
        )
    ]