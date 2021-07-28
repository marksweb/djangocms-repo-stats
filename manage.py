#!/usr/bin/env python
import os
import sys

from django.core import management

sys.path.append(
    os.path.join(os.path.dirname(__file__), 'djangocms_repo_stats')
)
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

if __name__ == "__main__":
    management.execute_from_command_line()
