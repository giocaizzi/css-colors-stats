import pytest
from css_colors_stats.parser import parse_css_for_colors


@pytest.mark.parametrize("color_format", ["ciao", ["ciao"], ["rgb", "ciao"]])
def test_parse_invalid_color_format(color_format):
    with pytest.raises(ValueError):
        parse_css_for_colors(HEX, color_format)


HEX = "body { background-color: #fff; color: #000; }"
RGB = "body { background-color: rgb(190,190,190); color: rgb(190,190,190); }"
HEXXX = """
body {
    background-color: #fff;
    color: #000;
}

main {
    background-color: #fff;
    color: #101010;
}

a {
    background-color: #101010;
}
"""
HEX_RGB = "body { background-color: #fff; color: rgb(190,190,190); }"


@pytest.mark.parametrize(
    "string,color_type",
    [(HEX, "hex"), (HEX, ["hex"]), (HEX, ["hex", "rgb"]), (RGB, "rgb")],
)
def test_parse_single_color_type(string: str, color_type: str):
    """test parsing for a single colortype

    result is a dict with only one nested dict.

    Tested effects:
    - requesting parsing in colortypes that are not present would not return a dict
    """
    result = parse_css_for_colors(string, color_format=color_type)
    # test result is a dict
    assert isinstance(result, dict)
    # that has only the corresponding color_type dict
    assert len(result) == 1
    assert any([isinstance(result[x], list) for x in result])


def test_parse_multiple_color_types():
    """test multiple color types without target specifications

    Tested effects:
    - result length is as long as the compatible color types found
    """
    result = parse_css_for_colors(HEX_RGB)
    assert len(result) == 2


def test_parse_result_sorting():
    """test that the result is sorted by descending count"""
    result = parse_css_for_colors(HEXXX)
    for color_type in result:
        check_order = [
            result[color_type][i]["count"] >= result[color_type][i + 1]["count"]
            for i in range(len(result[color_type]) - 1)
        ]
        assert all(check_order)
