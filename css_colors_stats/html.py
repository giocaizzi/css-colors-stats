"""html module"""

from typing import Union
from pathlib import Path
from typing import Dict


def build_html(matches: Dict[str, Dict[str, int]], file_path: Union[str, Path]) -> None:
    """Build an HTML file with the colors.

    Builds an HTML file with the colors and their counts.

    Args:
        matches (Dict[str, Dict[str, int]]): The color counts.
        file_path (Union[str, Path]): path to css file
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
    with open(Path(file_path.parent, file_path.stem + "_csscs.html"), "w") as file:
        file.write(html)
