import json

from dateutil.relativedelta import relativedelta
from django.utils.timezone import now
from github import Github

from .conf import (
    REPO_STATS_GITHUB_TOKEN,
    REPO_STATS_COMMIT_DAYS,
    REPO_STATS_CLOSED_DAYS
)


def get_repo_stats(user_repo):
    # using an access token
    g = Github(REPO_STATS_GITHUB_TOKEN)

    repo = g.get_repo(user_repo)

    dt_issues = now() + relativedelta(days=REPO_STATS_CLOSED_DAYS)
    issues_count = repo.get_issues(
        since=dt_issues,
        state='closed'
    ).totalCount

    dt_commits = now() + relativedelta(days=REPO_STATS_COMMIT_DAYS)
    commit_count = repo.get_commits(since=dt_commits).totalCount

    data = {
        'commit_count': commit_count,
        'forks_count': repo.forks,
        'issues_count': issues_count,
        'stars_count': repo.stargazers_count,
    }

    return json.dumps(data)
