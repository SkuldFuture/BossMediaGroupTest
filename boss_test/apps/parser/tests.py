from unittest.mock import patch

from boss_test.apps.parser.astana_hub_parser import parse_10_astana_hub_html, astana_hub_parser


def test_parse_astana_hub_html():
    html = """
    <html><body><table><tbody>
        <tr><td></td><td></td><td></td><td></td><td></td><td>Company A</td></tr>
        <tr><td></td><td></td><td></td><td></td><td></td><td>Company B</td></tr>
    </tbody></table></body></html>
    """

    result = parse_10_astana_hub_html(html)
    assert result == ["Company A", "Company B"]


@patch("boss_test.apps.parser.services.fetch_astana_hub_html")
def test_astana_hub_parser_success(mock_fetch):
    mock_fetch.return_value = """
    <html><body><table><tbody>
        <tr><td></td><td></td><td></td><td></td><td></td><td>Company X</td></tr>
    </tbody></table></body></html>
    """
    result = astana_hub_parser()
    assert result == ["Company X"]
