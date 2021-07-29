Settings
========

You must set ``REPO_STATS_GITHUB_TOKEN`` in your project settings to your `github access token`_ so that you can get statistics.

The default settings are;

.. code-block:: python

   REPO_STATS_COMMIT_DAYS = -30

   REPO_STATS_CLOSED_DAYS = -30

Commits
*******

The stats include the number of commits since a given day, where the default for ``REPO_STATS_COMMIT_DAYS`` is 30 days ago.


Closed issues
*************

The stats include the number of closed issues since a given day, where the default for ``REPO_STATS_CLOSED_DAYS`` is 30 days ago.


.. _github access token: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token