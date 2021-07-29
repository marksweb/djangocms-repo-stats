.. _cms_plugins:

CMS Plugins
===========

``GithubRepoStatsPlugin``
-------------------------

This is the primary plugin for getting statistics from github.

name
----

The plugin takes a ``name`` value which is the username & repo name from github.
For example, the URL for this application is https://github.com/marksweb/djangocms-repo-stats so the plugin
``name`` would be ``marksweb/djangocms-repo-stats``.


data
----

The data received from github is saved to a ``JSONField`` during a ``pre_save`` signal handler.

.. module:: djangocms_repo_stats.cms_plugins
   :synopsis: Signals sent by the moderation.
