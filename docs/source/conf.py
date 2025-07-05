# -*- coding: utf-8 -*-
import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

sys.path.insert(0, root)

sys.path.insert(0, os.path.join(root, 'vendor'))


# -- Project information -----------------------------------------------------
project   = 'cop_rubika_bot'
author    = 'Ali'
release   = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'myst_parser',
]

templates_path   = ['_templates']
exclude_patterns = ['rubpy/bots/*']

# پشتیبانی از فایل‌های rst و md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md' : 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme       = 'sphinx_rtd_theme'
html_static_path = ['_static']