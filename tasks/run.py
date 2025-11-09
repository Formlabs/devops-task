"""Run tasks for local and Docker execution."""

from invoke import task


@task
def local(ctx):
    """Run the Flask application locally with gunicorn."""
    ctx.run("uv run gunicorn --bind 0.0.0.0:8080 -w 2 helloapp.app:app")


@task
def docker(ctx):
    """Run the latest built Docker container."""
    ctx.run("podman run -p 8080:8080 helloapp:latest")
