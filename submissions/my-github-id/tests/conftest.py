import pytest
from pathlib import Path
import os

# Ensure src is on path when running tests from repo root
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in os.sys.path:
    os.sys.path.insert(0, str(SRC))


@pytest.fixture(autouse=True)
def set_test_env(tmp_path, monkeypatch):
    # Use a temp env for tests
    monkeypatch.setenv("API_BASE_URL", "http://localhost:8123")
    monkeypatch.setenv("API_TIMEOUT", "5")
    return True
