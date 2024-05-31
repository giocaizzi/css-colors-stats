import argparse
import json
from typing import Dict, List, Union
import re
from collections import Counter

search_patterns = {
    "hex": r"#(?:[0-9a-fA-F]{3}){1,2}\b",
    # "rgb": r"rgb\(\s*(\d+),\s*(\d+),\s*(\d+)\s*\)",
    # "rgba": r"rgba\(\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d*\.?\d+)\s*\)",
    # "hsl": r"hsl\(\s*(\d+),\s*(\d+)%,\s*(\d+)%\s*\)",
    # "hsla": r"hsla\(\s*(\d+),\s*(\d+)%,\s*(\d+)%\s*,\s*(\d*\.?\d+)\s*\)",
}


def parse_css_for_colors(
    css_content: str,
    color_format: Union[None, str, List[str]] = None,
) -> Dict[str, int]:

    if color_format is None:
        color_format = ["hex"]
    elif isinstance(color_format, str):
        color_format = [color_format]

    matches = {"hex": {}, "rgb": {}, "rgba": {}, "hsl": {}, "hsla": {}}

    for color_type in color_format:
        # Find all color occurrences
        matches[color_type] = Counter(
            re.findall(search_patterns[color_type], css_content)
        )

    # Sort each dictionary by decreasing values
    for color_type in matches:
        matches[color_type] = dict(
            sorted(matches[color_type].items(), key=lambda item: item[1], reverse=True)
        )
    return matches


def main(html=True):
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


def _build_html(matches):

    # Start the HTML file
    html = "<html><body>"

    for color_type in matches:
        html += f"<h1>{color_type}</h1>"
        # Add a div for each color
        for color in matches[color_type]:
            html += f'<div style="background-color:{color};width:100px;height:100px;">{color}:{matches[color_type][color]}</div>'

    # End the HTML file
    html += "</body></html>"

    # Write the HTML file
    with open("colors.html", "w") as file:
        file.write(html)


if __name__ == "__main__":
    main()