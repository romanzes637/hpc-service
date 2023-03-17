import pytest


def test_ping_hpc(client):
	response = client.get("/jobs/ping_hpc")
	assert response.status_code == 200
	assert response.json() == {"pong": True}
