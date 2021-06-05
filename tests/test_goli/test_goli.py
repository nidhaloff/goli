import pytest
from goli.cookiecutters import CookieCutterTemplates


@pytest.mark.parametrize(
    ("language", "topic", "repo"),
    [
        (
            "python",
            "package",
            "https://github.com/TezRomacH/python-package-template",
        ),
    ],
)
def test_get_template(language, topic, repo):
    """Example test with parametrization."""
    assert CookieCutterTemplates.get_template(language, topic) == repo
