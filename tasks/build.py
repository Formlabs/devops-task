"""Build tasks for container images."""

from invoke import task


@task
def build(ctx):
    """Build container image with buildah."""
    ctx.run("buildah build -t helloapp:latest .")


@task
def push(ctx, registry="localhost"):
    """Push container image to registry."""
    ctx.run(f"buildah push helloapp:latest {registry}/helloapp:latest")
