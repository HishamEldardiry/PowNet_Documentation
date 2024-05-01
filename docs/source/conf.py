import sys
import os
import re

# -- Project information

project = 'PowNet'
copyright = '2024, Critical Infrastricture Systems Lab, Cornell University'
author = 'Critical Infrastricture Systems Lab, Cornell University'

release = '2.0'
version = '2.0.0'

# -- General configuration

github_username = 'HishamEldardiry'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.viewcode',
    'sphinx_toolbox',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'


# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- customize the CSS styling
def setup(app):
        app.add_css_file('custom.css')
