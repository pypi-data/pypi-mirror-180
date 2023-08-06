#!/usr/bin/env python
import typer
from databricks_cli.sdk.api_client import ApiClient
from tabulate import tabulate

import fish_dbjob.config as config
from fish_dbjob.core.jobs_service import Job, JobsService
from fish_dbjob.core.version import package_version

app = typer.Typer(context_settings=dict(help_option_names=["-h", "--help"]))


def version_callback(value: bool):
    if value:
        typer.echo(f'Version: {package_version}')
        raise typer.Exit()


@app.callback()
def common(
        version: bool = typer.Option(None, '--version', '-v', callback=version_callback, help=package_version),
):
    pass


@app.command()
def jobs(
        name_filter: str = typer.Option(None, help='find jobs by name, case insensitively'),
        profile: str = typer.Option('DEFAULT', help='profile name in ~/.databrickscfg')
):
    '''Databricks jobs
    '''
    host, token = config.get(profile)

    api_client = ApiClient(host=host, token=token, api_version="2.1")
    service = JobsService(api_client)

    jobs = service.jobs(name_filter)

    print(tabulate(_jobs_to_table(jobs), tablefmt='plain', disable_numparse=True))


def _jobs_to_table(jobs: [Job]):
    ret = []
    for j in jobs:
        ret.append((j.id, j.name, j.tags))
    return sorted(ret, key=lambda j: j[1].lower())


if __name__ == "__main__":
    app()
