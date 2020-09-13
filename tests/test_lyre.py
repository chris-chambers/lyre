from lyre import __version__
from pathlib import Path
import toml


def test_version():
    project = toml.load(Path(__file__).parent.parent.joinpath('pyproject.toml'))
    assert __version__ == project['tool']['poetry']['version']
