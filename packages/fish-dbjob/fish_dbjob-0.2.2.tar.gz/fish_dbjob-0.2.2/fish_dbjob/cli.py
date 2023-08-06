#!/usr/bin/env python

from databricks_cli.sdk.api_client import ApiClient

from fish_dbjob.core import core
import typer
from fish_dbjob.core.version import package_version
import fish_dbjob.cofig as config

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo(f'Version: {package_version}')
        raise typer.Exit()

@app.callback()
def common(
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass

@app.command()
def jobs(name: str=None, profile='DEFAULT'):
    host, token = config.get(profile)

    api_client = ApiClient(host=host, token=token, api_version="2.1")
    core.jobs(api_client, name)


if __name__ == "__main__":
    app()
