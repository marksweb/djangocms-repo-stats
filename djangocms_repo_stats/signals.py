import logging

from django.core.cache import cache
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from github import UnknownObjectException

from .models import GithubRepoPlugin
from .utils import get_repo_stats

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=GithubRepoPlugin)
def pre_delete_post(sender, instance, **kwargs):
    key = "cache_key"
    cache.delete(key)


@receiver(pre_save, sender=GithubRepoPlugin)
def post_save_post(sender, instance, **kwargs):
    key = "cache_key"
    cache.delete(key)
    try:
        stats = get_repo_stats(instance.name)
        instance.data = stats
    except UnknownObjectException:
        logger.error(f"Invalid github repository: {instance.name}")

