# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import cubesat_specs

project = "cubesat-specs"
copyright = "2026, Julius Pinsker"
author = "Julius Pinsker"
release = cubesat_specs.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "myst_parser",
]

autodoc_member_order = "bysource"
autodoc_typehints = "description"

suppress_warnings = ["myst.xref_missing", "ref.python"]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -----------------------------------------------------

html_theme = "furo"
html_title = "cubesat-specs"
html_static_path = ["_static"]
