from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GithubRepoPlugin


@plugin_pool.register_plugin
class GithubRepoStatsPlugin(CMSPluginBase):
    """
    Github repo stats plugin.
    """
    name = _("Github repo stats")
    model = GithubRepoPlugin
    cache = True
    readonly_fields = (
        'data',
    )

    def get_render_template(self, context, instance, placeholder):
        return f'djangocms_repo_stats/{instance.template}/stats.html'

    def render(self, context, instance, placeholder):
        """Render the plugin."""
        context = super().render(context, instance, placeholder)
        return context
