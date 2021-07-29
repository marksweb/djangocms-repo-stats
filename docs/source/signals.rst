.. _signals:

Signals
=======


.. module:: djangocms_repo_stats.signals
   :synopsis: Signals sent by the moderation.

The :mod:`djangocms_repo_stats.signals` module defines a set of signals sent by
Django CMS Repo Stats.


pre_delete
----------

Clear cache.

pre_save
--------

Clear cache & collect data from github, saving it to the instance ``data`` field.
