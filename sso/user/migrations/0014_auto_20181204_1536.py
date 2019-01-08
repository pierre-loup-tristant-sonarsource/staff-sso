# Generated by Django 2.0.8 on 2018-12-04 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_accessprofile_saml2_applications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessprofile',
            name='oauth2_applications',
            field=models.ManyToManyField(blank=True, related_name='access_profiles', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
        migrations.AlterField(
            model_name='accessprofile',
            name='saml2_applications',
            field=models.ManyToManyField(blank=True, related_name='access_profiles', to='samlidp.SamlApplication'),
        ),
    ]
