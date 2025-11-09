"""Code quality and security check tasks."""

from invoke import task


@task
def lint(ctx):
    """Run ruff linting and format checks."""
    ctx.run("uv run ruff check .")
    ctx.run("uv run ruff format --check .")


@task
def format(ctx):
    """Auto-format code with ruff."""
    ctx.run("uv run ruff format .")
    ctx.run("uv run ruff check --fix .")


@task
def type_check(ctx):
    """Run pyrefly type checking."""
    ctx.run("uv run pyrefly check")


@task
def security(ctx):
    """Run bandit security checks."""
    ctx.run("uv run bandit -r helloapp/")


@task
def helm_lint(ctx):
    """Run helm lint on the chart."""
    ctx.run("helm lint chart")
