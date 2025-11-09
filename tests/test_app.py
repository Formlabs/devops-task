"""Tests for the Flask application."""

from helloapp.app import hello_world


def test_hello_world():
    """Test the hello_world function returns the expected greeting."""
    result = hello_world()
    assert "Hello" in result, "Endpoint is not polite enough."
    assert "World" in result


def test_hello_endpoint(flask_client):
    """Test the root endpoint returns 200 and contains Hello."""
    response = flask_client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data
    assert b"World" in response.data


def test_hello_endpoint_content_type(flask_client):
    """Test the root endpoint returns HTML content type."""
    response = flask_client.get("/")
    assert response.content_type.startswith("text/html")
