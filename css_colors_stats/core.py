"""Core module for the css_colors_stats package.

This module contains the core functions for the css_colors_stats package.

Example:
    Parse a CSS file for colors and save the color counts to a json file
    and an HTML file.

        $ python -m css_colors_stats.core test.css
"""

import argparse
import json
from typing import Dict, List, Union
import re
from collections import Counter

SEARCH_PATTERNS = {
    "hex": r"#(?:[0-9a-fA-F]{3}){1,2}\b",
    # "rgb": r"rgb\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)",
    # "rgba": r"rgba\(\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d*\.?\d+)\s*\)",
    # "hsl": r"hsl\(\s*(\d+),\s*(\d+)%,\s*(\d+)%\s*\)",
    # "hsla": r"hsla\(\s*(\d+),\s*(\d+)%,\s*(\d+)%\s*,\s*(\d*\.?\d+)\s*\)",
}


def parse_css_for_colors(
    css_content: str,
    color_format: Union[None, str, List[str]] = None,
) -> Dict[str, Dict[str, int]]:
    """Parse a CSS file for colors.

    Parses a CSS file for colors and returns the counts of each color.

    Available color formats:
    - hex
    - rgb (to be implemented)
    - rgba (to be implemented)
    - hsl (to be implemented)
    - hsla (to be implemented)

    Args:
        css_content (str): The content of the CSS file.
        color_format (Union[None, str, List[str]], optional): The color format
            to search for. Defaults to None.

    Returns:
        Dict[str, Dict[str, int]]: Dictionary with
            the color counts for each color format.

    Raises:
        ValueError: If the color format is invalid.

    Example:
        Parse a CSS file for hex colors

            >>> css_content = 'body { background-color: #fff; color: #000; }'
            >>> parse_css_for_colors(css_content)
            {'hex': {'#fff': 1, '#000': 1}, 'rgb': {}, 'rgba': {}, 'hsl': {}, 'hsla': {}} # noqa
    """

    if color_format is None:
        color_format = ["hex"]
    elif isinstance(color_format, str) and color_format in SEARCH_PATTERNS:
        color_format = [color_format]
    elif isinstance(color_format, list):
        pass
    else:
        raise ValueError("Invalid color format.")

    matches = {"hex": {}, "rgb": {}, "rgba": {}, "hsl": {}, "hsla": {}}

    # Find all color occurrences in the CSS content
    for color_type in color_format:
        matches[color_type] = Counter(
            re.findall(SEARCH_PATTERNS[color_type], css_content)
        )

    # Sort each dictionary by decreasing values
    for color_type in matches:
        matches[color_type] = dict(
            sorted(matches[color_type].items(), key=lambda item: item[1], reverse=True)
        )
    return matches


def main(html: bool = True) -> None:
    """Main function for the CLI.

    Parses a CSS file for colors and saves the color counts to a json file.

    Args:
        html (bool, optional): If True, an HTML file with the colors will be created.
            Defaults to True.

    Example:
        Parse a CSS file for colors and save the color counts to a json file.
        Save an HTML file with the colors.

            $ python -m css_colors_stats.core test.css
    """
    parser = argparse.ArgumentParser(description="Process a CSS file.")
    # Add the arguments
    parser.add_argument(
        "FilePath", metavar="filepath", type=str, help="the path to the CSS file"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Read CSS file
    with open(args.FilePath, "r", encoding="utf-8") as file:
        css_content = file.read()

    # Parse CSS content for colors
    color_counts = parse_css_for_colors(css_content)

    if html:
        _build_html(color_counts)

    # Save color counts to a json file
    with open("color_counts.json", "w") as file:
        json.dump(color_counts, file, indent=4)

    # # Print color counts
    # for color_type in color_counts:
    #     for color, count in color_counts[color_type].items():
    #         print(f"{color_type}: {color} - {count}")


def _build_html(matches: Dict[str, Dict[str, int]]) -> None:
    """Build an HTML file with the colors.

    Builds an HTML file with the colors and their counts.

    Args:
        matches (Dict[str, Dict[str, int]]): The color counts.
    """

    # Start the HTML file
    html = "<html><body>"

    for color_type in matches:
        html += f"<h1>{color_type}</h1>"
        # Add a div for each color
        for color in matches[color_type]:
            html += f'<div style="background-color:{color};width:100px;height:100px;">{color}:{matches[color_type][color]}</div>'  # noqa

    # End the HTML file
    html += "</body></html>"

    # Write the HTML file
    with open("colors.html", "w") as file:
        file.write(html)


if __name__ == "__main__":
    main()
