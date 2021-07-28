from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models import CMSPlugin

try:
    # >= django 3.1
    from django.db.models import JSONField
except ImportError:
    # < django 3.1
    from django_extensions.db.fields.json import JSONField


# Check ``settings.py`` for additional templates.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_REPO_STATS_TEMPLATES',
        [],
    )
    return choices


class GithubRepoPlugin(CMSPlugin):
    """ Repo stats """
    name = models.CharField(
        max_length=255,
        help_text=_("Repo name as user/repo")
    )
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    data = JSONField(
        blank=True,
        help_text=_("Data from github")
    )

    class Meta:
        verbose_name = _("github repo")
        verbose_name_plural = _("github repos")

    def __str__(self):
        return f"{self.name} stats"
