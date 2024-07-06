import pytest
from fastapi.testclient import TestClient

from jatlist_api.app import app


@pytest.fixture
def client():
    return TestClient(app)
