HELPER_SETTINGS = {
    "INSTALLED_APPS": [
        "djangocms_repo_stats",
    ],
    # As advised, we can disable migrations in tests. This will improve
    # test performance and removes the need for test apps to provide migrations
    "MIGRATION_MODULES": {
        "auth": None,
        "cms": None,
        "menus": None,
        "djangocms_repo_stats": None,
    },
}


def run():
    from djangocms_helper import runner

    runner.cms("djangocms_repo_stats")


if __name__ == "__main__":
    run()