import pytest
from css_colors_stats.core import parse_css_for_colors


@pytest.mark.parametrize("color_format", ["ciao", ["ciao"], ["rgb", "ciao"]])
def test_parse_invalid_color_format(color_format):
    with pytest.raises(ValueError):
        parse_css_for_colors(HEX, color_format)


HEX = "body { background-color: #fff; color: #000; }"
RGB = "body { background-color: rgb(190,190,190); color: rgb(190,190,190); }"


@pytest.mark.parametrize("string,color_type", [(HEX, "hex"), (RGB, "rgb")])
def test_parse(string: str, color_type: str):
    result = parse_css_for_colors(string)
    # test result is a dict
    assert isinstance(result, dict)
    # test nested dict
    assert isinstance(result[color_type], dict)
    # test counts
    # assert any([not isinstance(x, int) for x in result[color_type].values()])
