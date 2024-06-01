"""Core module for the css_colors_stats package.
"""

from pathlib import Path
import argparse
import json

from css_colors_stats.html import build_html
from css_colors_stats.parser import parse_css_for_colors


def main(html: bool = True) -> None:
    """Main function for the CLI.

    Parses a CSS file for colors and saves the color counts to a json file.

    Args:
        html (bool, optional): If True, an HTML file with the colors will be created.
            Defaults to True.

    Example:
        Parse a CSS file for colors and save the color counts to a json file.
        Save an HTML file with the colors.

            $ css-colors-stats test.css
    """
    parser = argparse.ArgumentParser(description="Process a CSS file.")
    # Add the arguments
    parser.add_argument(
        "FilePath", metavar="filepath", type=str, help="the path to the CSS file"
    )

    # Parse the arguments
    args = parser.parse_args()

    # FilePath
    file_path = Path(args.FilePath)

    # Read CSS file
    with open(file_path, "r", encoding="utf-8") as file:
        css_content = file.read()

    # Parse CSS content for colors
    color_counts = parse_css_for_colors(css_content)

    # Save colors to HTML file
    if html:
        build_html(color_counts, file_path)

    # Save color counts to a json file
    with open(Path(file_path.parent, file_path.stem + "_csscs.json"), "w") as file:
        json.dump(color_counts, file, indent=4)
