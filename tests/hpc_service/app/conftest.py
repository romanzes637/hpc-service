from fastapi.testclient import TestClient
import pytest

from hpc_service.app.main import app
from hpc_service.app.core.config import settings


@pytest.fixture
def client():
    return TestClient(app, base_url=f"http://{settings.API_V1_STR}")
