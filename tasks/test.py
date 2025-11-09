"""Testing tasks."""

from invoke import task


@task
def test(ctx):
    """Run tests with pytest."""
    ctx.run("uv run pytest")
