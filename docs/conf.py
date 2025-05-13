import sys

# ----------------------------------------------------------
# Extensions
# ----------------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid',
    # 'feature_maturity_warnings',
    # 'sphinxext.rediraffe',
    # 'auth_restricted_section',
    # 'sphinx.ext.extlinks',
    # 'sphinx-copybutton',
    # 'sphinx-notfound-page',
    # 'side_by_side'
]

# Intersphinx
# -----------
intersphinx_mapping = {
    "v114": ("https://isovalent-microovn.readthedocs-hosted.com/v1.14/", None),
    "v115": ("https://isovalent-microovn.readthedocs-hosted.com/v1.15/", None),
    "v116": ("https://isovalent-microovn.readthedocs-hosted.com/v1.16/", None),
    "v117": ("https://isovalent-microovn.readthedocs-hosted.com/latest/", None)
}
#   Prevent resolving of references to external locations.
#   https://www.sphinx-doc.org/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]

# Sphinxcontrib-mermaid
# ---------------------
mermaid_version = "11.6.0"

# MyST parser
# -----------
myst_enable_extensions = [
    'substitution',
    'colon_fence'
]

# ----------------------------------------------------------
# General configuration
# ----------------------------------------------------------

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.sphinx'
]

## Often-used links
rst_epilog = '''
.. include:: /reuse/links.txt
'''

## reStructuredText and Markdown extensions
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

## Linkchecker
linkcheck_anchors_ignore_for_url = [
    r'https://github\.com/.*'
]

linkcheck_ignore = [
    r'.*cisa\.gov.*'
]

linkcheck_timeout = 120
linkcheck_retries = 3

# ----------------------------------------------------------
# Styling
# ----------------------------------------------------------

## Theme configuration
html_theme = 'furo'
html_last_updated_fmt = ''
html_permalinks_icon = '¶'

html_theme_options = {
    'sidebar_hide_name': True
    }

# ----------------------------------------------------------
# Additional files
# ----------------------------------------------------------

html_static_path = ['.sphinx/_static']

html_css_files = [
    'custom.css',
    'header.css'
]
