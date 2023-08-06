#!/usr/bin/env python3
#
# Copyright 2022 Graviti. Licensed under MIT License.
#

"""Implementation of hit clone."""

import os
import sys
from subprocess import CalledProcessError, run
from typing import Any, Dict, List, Optional

import click
from github import Github
from github.GithubException import UnknownObjectException

from hit.utility import ENV, fatal_and_kill, read_config

_PRECOMMIT_CONFIG_PATH = ".pre-commit-config.yaml"


def _implement_clone(repository: str, directory: Optional[str]) -> None:
    token = read_config()["github"]["token"]
    github = Github(token)
    name = _get_repo_name(repository)
    try:
        origin_repo = github.get_repo(name)
    except UnknownObjectException:
        fatal_and_kill(f"Repository '{name}' not found!")

    click.secho("> Forking:", bold=True)

    if origin_repo.visibility == "private":
        click.secho(f"Repository '{name}' is private, skip the fork process.\n")
        target_repo = origin_repo
    else:
        target_repo = origin_repo.create_fork()

        click.echo(f"Repository forked: {click.style(target_repo.full_name, bold=True)}\n")

    directory = directory if directory else name.split("/", 1)[1]
    try:
        click.secho("> Cloning:", bold=True)
        run(["git", "clone", target_repo.ssh_url, directory], env=ENV, check=True)

        os.chdir(directory)

        click.secho("\n> Setting upstream:", bold=True)
        run(["git", "remote", "add", "upstream", origin_repo.ssh_url], env=ENV, check=True)
        run(
            ["git", "config", "--local", "remote.upstream.gh-resolved", "base"], env=ENV, check=True
        )

        click.echo(f"Remote added: {click.style(origin_repo.ssh_url, underline=True)}\n")

    except CalledProcessError:
        sys.exit(1)

    if os.path.exists(_PRECOMMIT_CONFIG_PATH):
        click.secho("> Installing 'pre-commit' scripts:", bold=True)
        _install_precommit_scripts()
        click.echo()

    click.secho("> Success!", fg="green")


def _get_repo_name(repository: str) -> str:
    name = repository

    if repository.startswith("https://github.com/"):
        name = name[19:]
    elif repository.startswith("git@github.com:"):
        name = name[15:]
    else:
        return name

    name = "/".join(name.split("/", 2)[:2])

    if name.endswith(".git"):
        name = name[:-4]

    return name


def _install_precommit_scripts() -> None:
    try:
        # pylint: disable=import-outside-toplevel
        from pre_commit.clientlib import load_config
        from pre_commit.commands.install_uninstall import install
        from pre_commit.store import Store
    except ModuleNotFoundError:
        click.secho(
            f"'{_PRECOMMIT_CONFIG_PATH}' is found in the repo, but 'pre-commit' is not installed.\n"
            "Skip the 'pre-commit' scripts installation phrase.\n",
            fg="yellow",
        )

        click.echo(
            "To install 'pre-commit', run:\n"
            "  $ pip install pre-commit\n"
            "\n"
            "To install the 'pre-commit' scripts for the repo, run:\n"
            "  $ pre-commit install [-t {hook types}]\n"
            "\n"
            f"Check {click.style('https://pre-commit.com/index.html', underline=True)} "
            "for more info."
        )
        return

    config: Dict[str, Any] = load_config(_PRECOMMIT_CONFIG_PATH)

    stages: List[str] = config["default_install_hook_types"].copy()
    for repo in config["repos"]:
        for hook in repo["hooks"]:
            stages.extend(hook.get("stages", []))

    install(_PRECOMMIT_CONFIG_PATH, Store(), stages)
