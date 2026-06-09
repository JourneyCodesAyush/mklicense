import os
import pytest

from tempfile import TemporaryDirectory

ROOT_PATH = os.getcwd()

@pytest.fixture
def tmp_dir():
    sample_dir = TemporaryDirectory(dir=ROOT_PATH)
    try:
        yield sample_dir.name
    finally:
        sample_dir.cleanup()
