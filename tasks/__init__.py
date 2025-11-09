"""Invoke tasks for building, testing, and running the application."""

from invoke import Collection, Config, task

from . import build, check, run, test

config = Config(defaults={"run": {"pty": True}})

ns = Collection()
ns.add_collection(Collection.from_module(build))
ns.add_collection(Collection.from_module(check))
ns.add_collection(Collection.from_module(run))
ns.add_collection(Collection.from_module(test))


@task
def ci(ctx):
    """Run all CI checks (lint, type-check, security, test, helm-lint)."""
    from .check import helm_lint, lint, security, type_check
    from .test import test

    lint(ctx)
    type_check(ctx)
    security(ctx)
    test(ctx)
    helm_lint(ctx)


ns.add_task(ci)
ns.configure(config)
