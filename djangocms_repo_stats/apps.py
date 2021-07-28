from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RepoStatsConfig(AppConfig):
    """ Application configuration """
    name = "djangocms_repo_stats"
    verbose_name = _("django CMS Repo Stats")

    def ready(self):
        """ Load signals when the application is ready """
        import djangocms_repo_stats.signals  # noqa: F401
