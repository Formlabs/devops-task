"""Invoke tasks for building, testing, and running the application."""

from invoke import Collection, Config, task

from . import build, check, test

config = Config(defaults={"run": {"pty": True}})

ns = Collection()
ns.add_collection(Collection.from_module(build))
ns.add_collection(Collection.from_module(check))
ns.add_collection(Collection.from_module(test))


@task
def run(ctx):
    """Run the Flask application with gunicorn."""
    ctx.run("uv run gunicorn --bind 0.0.0.0:8080 -w 2 helloapp.app:app")


@task
def ci(ctx):
    """Run all CI checks (lint, type-check, security, test)."""
    from .check import lint, security, type_check
    from .test import test

    lint(ctx)
    type_check(ctx)
    security(ctx)
    test(ctx)


ns.add_task(run)
ns.add_task(ci)
ns.configure(config)
