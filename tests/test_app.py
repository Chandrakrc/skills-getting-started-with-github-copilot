"""
Backend FastAPI tests for app.py using the AAA (Arrange-Act-Assert) pattern.
"""
import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

client = TestClient(app)

def test_get_activities():
    # Arrange
    # (No special setup required for this test)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    test_email = "testuser@mergington.edu"
    test_activity = next(iter(client.get("/activities").json().keys()))

    # Act - Signup
    signup_resp = client.post(f"/activities/{test_activity}/signup?email={test_email}")

    # Assert - Signup
    assert signup_resp.status_code == 200
    assert "message" in signup_resp.json()

    # Act - Unregister
    unregister_resp = client.post(f"/activities/{test_activity}/unregister?email={test_email}")

    # Assert - Unregister
    assert unregister_resp.status_code == 200
    assert "message" in unregister_resp.json()
