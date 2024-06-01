"""css-colors-stats

Quickly extract and count colors from CSS files.

Example:
    Parse a CSS file for colors and save the color counts to a json file
    and an HTML file.

        $ css-colors-stats test.css
"""

from .core import main

__all__ = ["main"]
