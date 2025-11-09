"""Build tasks for container images."""

from invoke import task


@task
def build(ctx):
    """Build container image with buildah."""
    ctx.run("buildah build -t helloapp:latest .")
