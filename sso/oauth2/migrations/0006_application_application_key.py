# Generated by Django 2.0.8 on 2018-11-15 18:28

from django.db import migrations, models
from django.utils.text import slugify


def populate_application_key(apps, schema_editor):
    Application = apps.get_model('oauth2', 'Application')

    for app in Application.objects.all():
        app.application_key = slugify(app.name)
        app.save()


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0005_application_allow_tokens_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_key',
            field=models.SlugField(default='', unique=False, verbose_name='unique text id'),
            preserve_default=False,
        ),
        migrations.RunPython(populate_application_key),
    ]
