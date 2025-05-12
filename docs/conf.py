import sys

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

############################################################
### Extensions
############################################################

extensions = [
    'sphinx_design',
    'sphinx_tabs.tabs',
    'related-links',
    'custom-rst-roles',
    'sphinx_copybutton',
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid'
]

### Configuration for extensions

# Intersphinx
intersphinx_mapping = {
    "v114": ("https://isovalent-microovn.readthedocs-hosted.com/v1.14/", None),
    "v115": ("https://isovalent-microovn.readthedocs-hosted.com/v1.15/", None),
    "v116": ("https://isovalent-microovn.readthedocs-hosted.com/v1.16/", None),
    "v117": ("https://isovalent-microovn.readthedocs-hosted.com/latest/", None),
}
# Prevent resolving of references to external locations.
# https://www.sphinx-doc.org/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]

# Mermaid and sphinxcontrib-mermaid
mermaid_version = "11.6.0"

# Additional MyST syntax
myst_enable_extensions = [
    'substitution',
    'deflist',
    'linkify'
]

############################################################
### General configuration
############################################################

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.sphinx',
]

rst_epilog = '''
.. include:: /reuse/links.txt
'''

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# For ignoring specific links
linkcheck_anchors_ignore_for_url = [
    r'https://github\.com/.*'
]

# URLs for the linkchecker to ignore
linkcheck_ignore = [r'.*cisa\.gov.*']

linkcheck_timeout = 120
linkcheck_retries = 3

############################################################
### Styling
############################################################

# Find the current builder
builder = 'dirhtml'
if '-b' in sys.argv:
    builder = sys.argv[sys.argv.index('-b')+1]

# Setting templates_path for epub makes the build fail
if builder == 'dirhtml' or builder == 'html':
    templates_path = ['.sphinx/_templates']

# Theme configuration
html_theme = 'furo'
html_last_updated_fmt = ''
html_permalinks_icon = '¶'

html_theme_options = {
    'sidebar_hide_name': True
    }

############################################################
### Additional files
############################################################

html_static_path = ['.sphinx/_static']

html_css_files = [
    'custom.css',
    'header.css'
]
