from setuptools import find_packages, setup

import djangocms_repo_stats


INSTALL_REQUIREMENTS = [
    "Django>=2.2,<4.0",
    "django-cms",
    "pygithub",
    "requests"
]

setup(
    name="djangocms-repo-stats",
    packages=find_packages(),
    include_package_data=True,
    version=djangocms_repo_stats.__version__,
    description=djangocms_repo_stats.__doc__,
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author="Mark Walker",
    author_email="theshow@gmail.com",
    url="http://github.com/marksweb/djangocms-repo-stats",
    license="BSD3",
    test_suite="tests.settings.run",
)
