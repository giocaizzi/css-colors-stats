import pytest
from css_colors_stats.core import parse_css_for_colors


@pytest.mark.parametrize("color_format", ["ciao", ["ciao"], ["rgb", "ciao"]])
def test_parse_invalid_color_format(color_format):
    with pytest.raises(ValueError):
        parse_css_for_colors(HEX, color_format)


HEX = "body { background-color: #fff; color: #000; }"


def test_parse_hex():
    result = parse_css_for_colors(HEX)
    assert isinstance(result, dict)
