"""this test file is mostly here to test that we can import the main module

importing may not work when we forgot to declare some dependencies.
"""

import re
from relay import main
import pytest


def test_get_version():
    version = main.get_version()
    print(f"VERSION {version!r}")
    assert re.match(r"^\d+", version), "version should start with a number"


@pytest.fixture
def write_config(tmp_path):
    """returns a function that writes a config file"""

    def write(config):
        p = tmp_path / "config.json"
        with open(p, "w") as f:
            f.write(config)
        return str(p)

    return write


def test_config(write_config):
    example_logging_config = """
    {
      "logging": {
        "loggers": {
          "relay.relay": {
            "level": "DEBUG"
          },
          "relay.streams": {
            "level": "INFO"
          }
        }
      }
    }
    """
    config = main.load_config(write_config(example_logging_config))
    print(config)
    assert config["logging"]["loggers"]["relay.relay"] == {"level": "DEBUG"}
    assert config["logging"]["loggers"]["relay.streams"] == {"level": "INFO"}
