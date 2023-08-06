from __future__ import annotations

import click

from clitools.config.config_files_initiatior import ConfigFilesInitiator
from clitools.core import Core


@click.group(invoke_without_command=True)
@click.pass_context
def clitools(ctx) -> None:
    if not ctx.invoked_subcommand:
        Core().run()


@clitools.command()
def init():
    ConfigFilesInitiator().init()
