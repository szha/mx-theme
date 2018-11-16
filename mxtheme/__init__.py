from os import path
from .card import CardDirective

__version__ = '0.2'
__version_full__ = __version__

package_dir = path.dirname(path.abspath(__file__))

def get_path():
    return package_dir

def setup(app):
    app.add_html_theme('mxtheme', package_dir)
