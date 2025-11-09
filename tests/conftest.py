"""Pytest configuration and fixtures for testing the Flask application."""

import pytest

from helloapp.app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a Flask application instance for testing."""
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )
    yield flask_app


@pytest.fixture
def flask_client(app):
    """Create a test client for the Flask application."""
    return app.test_client()
