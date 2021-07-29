# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'djangocms-repo-stats'
copyright = '2021, Mark Walker'
author = 'Mark Walker'

# The full version, including alpha/beta/rc tags
# release = djangocms_repo_stats.__version__
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinxcontrib.spelling',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'django': (
        'https://docs.djangoproject.com/en/3.2/',
        'https://docs.djangoproject.com/en/3.2/_objects/'
    ),
    'cms': ('https://docs.django-cms.org/en/latest/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

try:
    import furo

    html_theme = 'furo'
    html_theme_options = {
        "navigation_with_keys": True,
    }
except ImportError:
    html_theme = 'alabaster'

show_cloud_banner = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Spelling language.
spelling_lang = 'en_GB'

# Location of word list.
spelling_word_list_filename = 'spelling_wordlist'

spelling_ignore_pypi_package_names = True

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]