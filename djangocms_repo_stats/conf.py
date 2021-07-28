from django.conf import settings

REPO_STATS_GITHUB_TOKEN = getattr(
    settings, "REPO_STATS_GITHUB_TOKEN", None
)

REPO_STATS_COMMIT_DAYS = getattr(
    settings, "REPO_STATS_COMMIT_DAYS", -30
)

REPO_STATS_CLOSED_DAYS = getattr(
    settings, "REPO_STATS_CLOSED_DAYS", -30
)
