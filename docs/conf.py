# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import subprocess

project = 'Isovalent Networking for Kubernetes'
copyright = 'Isovalent'
author = 'Isovalent'

# Needed for sphinx.ext.extlinks
# Variable CILIUM_VERSION is located in the root of the docs directory
# cilium_version = open("CILIUM_VERSION", "r").read().strip()
# cilium_release = cilium_version[:cilium_version.rfind(".")]
# cilium_doc_version = "v" + cilium_release

# ----------------------------------------------------------
# Extensions
# ----------------------------------------------------------

sys.path.insert(0, os.path.abspath('_exts'))

import side_by_side
import auth_restricted_section

extensions = [
    # 'myst_parser',
    # 'sphinx_tabs.tabs',
    # 'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid',
    #
    # 'auth_restricted_section',
    # 'feature_maturity_warnings',
    # 'side_by_side',
    #
    # 'sphinxext.rediraffe',
    # 'sphinx-copybutton',
    # 'sphinx-notfound-page',
]

# sphinx.ext.intersphinx
# ----------------------
intersphinx_mapping = {
    "v114": ("https://isovalent-microovn.readthedocs-hosted.com/v1.14/", None),
    "v115": ("https://isovalent-microovn.readthedocs-hosted.com/v1.15/", None),
    "v116": ("https://isovalent-microovn.readthedocs-hosted.com/v1.16/", None),
    "v117": ("https://isovalent-microovn.readthedocs-hosted.com/latest/", None),
}
# Prevent resolving of references to external locations.
# https://www.sphinx-doc.org/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]

# sphinxcontrib.mermaid
# ---------------------
mermaid_version = "11.6.0"

# myst_parser
# -----------
# myst_enable_extensions = [
#     'substitution',
#     'colon_fence'
# ]
# myst_heading_anchors = 3
# suppress_warnings = ["myst.header", "ref.myst"]

# sphinx.ext.extlinks
# -------------------
# github_repo = 'https://github.com/cilium/cilium/'
# extlinks = {
#     'cilium-doc': ('https://docs.cilium.io/en/' + cilium_doc_version + "%s", ''),
#     'gh-issue': (github_repo + 'issues/%s', 'GitHub issue %s'),
# }

# ----------------------------------------------------------
# General configuration
# ----------------------------------------------------------

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.sphinx'
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = [
#     '**/_includes/**',
# ]

## Often-used links
# rst_epilog = '''
# .. include:: /reuse/links.txt
# '''

## reStructuredText and Markdown extensions
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

## Linkchecker
# linkcheck_anchors_ignore_for_url = [
#     r'https://github\.com/.*'
# ]

# linkcheck_ignore = [
#     r'.*cisa\.gov.*'
# ]

# linkcheck_timeout = 120
# linkcheck_retries = 3

# ----------------------------------------------------------
# Styling
# ----------------------------------------------------------

html_favicon = '_static/images/favicon.png'     # browser favicon
html_permalinks_icon = '🔗'                     # mouseover icon for page heading title links
html_copy_source = False                        # link to the current page's raw source file
                                                #   in the secondary (page) sidebar (RHS menu)


# Paths (relative to this directory) to custom static files. A custom file will
# overwrite an identically named built-in file.
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]             # files are relative to 'html_static_path'

# For the primary (section) sidebar (LHS menu), map page names
#   to template names - a null value removes the menu
html_sidebars = {
    "**": ["sidebar-nav-bs"]
}

### Theme-specific configuration
# https://pydata-sphinx-theme.readthedocs.io
# components: https://is.gd/xibtfW
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "logo": {
        "image_light": "_static/images/isovalent-logo-light-theme.png", # light mode logo
        "image_dark": "_static/images/isovalent-logo-dark-theme.png"    # dark mode logo
    },
    # "external_links": [
    #     {"name": "Kubernetes", "url": "https://kubernetes.io"},         # miscellaneous external links
    #     {"name": "Docker", "url": "https://docker.com"},
    #     {"name": "Linux", "url": "https://linux.org"}
    # ],
    "navbar_start": ["navbar-logo"],            # display components at start of navbar
    "navbar_center": ["navbar-nav"],            # display components at middle of navbar
    "navbar_persistent": ["search-field"],      # display components to the left of navbar_end; always visible
    "navbar_end": [],                           # display components at end of navbar
    "header_links_before_dropdown": 6,          # number of links in header before spilling over into the "More" dropdown
    "navigation_depth": 5,                      # maximum depth for menu dropdowns in the primary sidebar
    "primary_sidebar_end": [],                  # templates to use underneath the primary (section) sidebar (LHS menu)
    "secondary_sidebar_items": ["page-toc"],    # templates to use within the secondary (page) sidebar (RHS menu)
    "show_prev_next": False,                    # show previous and next buttons
    "back_to_top_button": False,                # show floating back-to-top button
    "footer_start": ["copyright"],              # built-in components to use at start of footer
    "footer_end": [],                           # built-in components to use at end of footer
    "surface_warnings": False                   # display theme warnings, deprecations, etc
}

## Add an announcement banner if the local branch is 'main'
command = ["git", "branch", "--show-current"]
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
branch = stdout.strip()
if branch == "main":
    html_theme_options["announcement"] = "<b>Attention:</b> These docs are built from the 'main' branch."
