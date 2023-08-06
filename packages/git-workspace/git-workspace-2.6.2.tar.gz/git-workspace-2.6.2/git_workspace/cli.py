import argparse
import logging
import os
import pathlib

import click

from git_workspace.configuration import init_workspace, search_workspace, read_configuration
from git_workspace.git import in_repository_operation, git_clone, ws_state, change_to_default_branch_and_update
from git_workspace.integrations.gitlab import sync_repositories
from git_workspace.directory_operations.cleanup import cleanup_to_archive

_AUTHOR = "Aki Mäkinen"
_LICENSE = "MIT"

WORKSPACE_DIR = None

DEFAULT_LOCATION = "$HOME/.local/bin"
SCRIPT_NAME = os.path.basename(__file__)

_DEBUG = os.getenv("DEBUG")


def disabled(msg):
    print(msg)
    exit(1)


def setup_loglevel():
    level = os.environ.get("LOGLEVEL")
    if level is None:
        return
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
        "FATAL": logging.FATAL
    }

    mapped_level = level_map.get(level)
    if mapped_level is None:
        print(f"Unsupported level {level}. Using the default.")
        return

    logging.basicConfig(level=mapped_level)


@click.group(context_settings={"obj": {}})
@click.pass_context
def main(ctx):
    """
    Git Workspace

    \b
    Copyright 2021 Aki Mäkinen
    https://gitlab.com/blissfulreboot/python/git-workspace
    Licensed under MIT license
    """
    ctx.ensure_object(dict)
    setup_loglevel()

    ws = search_workspace()
    if ws is None and ctx.invoked_subcommand not in ["init", "autocomplete"]:
        print("Workspace not found.")
        exit(1)

    configuration = {}
    repositories = {}
    if ws is not None:
        configuration = read_configuration().get("remote", {})
        repositories = read_configuration().get("repositories", [])

    ctx.obj["configuration"] = configuration
    ctx.obj["repositories"] = list(repositories)
    ctx.obj["ws"] = ws


@main.command(help="Initialize a new blank workspace")
@click.pass_context
def init(ctx):
    init_workspace()


@main.command(help="Clone the repositories listed in the workspace configuration")
@click.pass_context
def clone(ctx):
    ws = ctx.obj["ws"]
    reps = ctx.obj["repositories"]
    conf = ctx.obj["configuration"]

    git_clone(ws, reps, conf)


@main.command(help="Print the state of the repositories in the workspace")
@click.pass_context
def state(ctx):
    ws = ctx.obj["ws"]
    reps = ctx.obj["repositories"]

    ws_state(ws, reps)


@main.command(help="Run a command in each workspace git directory")
@click.argument("cmd", nargs=-1)
@click.pass_context
def command(ctx, cmd):
    ws = ctx.obj["ws"]
    repos = ctx.obj["repositories"]

    in_repository_operation(" ".join(cmd), repos, ws)


@main.command(help="Stash potential changes, switch to the default branch and pull the latest from remote. (Assumes that the remote name is origin)")
@click.pass_context
def default_and_update(ctx):
    ws = ctx.obj["ws"]
    repos = ctx.obj["repositories"]

    change_to_default_branch_and_update(repos, ws)


@main.command(help="Move repositories not included in the workspace configuration into an archive directory.")
@click.pass_context
def cleanup(ctx):
    ws = ctx.obj["ws"]
    repos = ctx.obj["repositories"]

    cleanup_to_archive(ws, repos)


@main.command(help="Sync the workspace to match the state of the gitlab group")
@click.option("--group", "-g", required=True, type=str, prompt="Group (leave blank to fetch all available)?", default="", help="Gitlab group path")
@click.option("--do-not-include-subgroups", is_flag=True, help="Include only the repositories directly under the group and ignore subgroups")
@click.option("--flatten", "-f", is_flag=True, prompt=True, help="Flatten the structure (by default creates a directory structure similar the group structure in Gitlab)")
@click.pass_context
def gitlab_sync(ctx, group, do_not_include_subgroups, flatten):
    ws = ctx.obj["ws"]
    sync_repositories(ws, group, do_not_include_subgroups, flatten)


@main.group()
def gitlab():
    pass


@gitlab.command("sync", help="Sync the workspace to match the state of the gitlab group")
@click.option("--group", "-g", required=True, type=str, prompt="Group (leave blank to fetch all available)?", default="", help="Gitlab group path")
@click.option("--do-not-include-subgroups", is_flag=True, help="Include only the repositories directly under the group and ignore subgroups")
@click.option("--flatten", "-f", is_flag=True, prompt=True, help="Flatten the structure (by default creates a directory structure similar the group structure in Gitlab)")
@click.pass_context
def gl_sync(ctx, group, do_not_include_subgroups, flatten):
    ws = ctx.obj["ws"]
    sync_repositories(ws, group, do_not_include_subgroups, flatten)

