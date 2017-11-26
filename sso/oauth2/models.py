from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from oauth2_provider.models import AbstractApplication


class Application(AbstractApplication):
    default_access_allowed = models.BooleanField(
        _('default access allowed'),
        default=False,
        help_text=_(
            'Allow all authenticated users to access this application'
        )
    )

    email_ordering = models.CharField(
        _('email ordering'),
        blank=True,
        null=True,
        max_length=255,
        help_text=_(
            ('A comma separated list of email domains, e.g "mobile.ukti.gov.uk, trade.gsi.gov.uk, fco.gov.uk" '
             'for users with multiple email addresses this list determines which email is sent to the application.')
        )
    )

    def get_email_order(self):
        ordering = self.email_ordering or getattr(settings, 'DEFAULT_EMAIL_ORDER', '')

        if not ordering:
            return []

        return [email.strip() for email in ordering.split(',')]
