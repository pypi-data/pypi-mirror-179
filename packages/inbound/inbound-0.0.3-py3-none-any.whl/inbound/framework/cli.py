import os
import webbrowser
from pathlib import Path

import click

from inbound import __version__ as version
from inbound.core.jobs import run_all_job_in_directory, run_job

here = os.getcwd()

LOGO = rf"""
dbc. v{version}
"""


@click.group(name="dbc")
@click.version_option(version, "--version", "-V", help="Show version and exit")
def dbc():
    """dbc is a CLI for running data ingestion and governance jobs. For more
    information, type ``dbc info``.
    """
    pass


@dbc.command()
def info():
    """Get more information about dbc."""
    click.secho(LOGO, fg="green")
    click.echo("Declarative data ingestion for dataproducts.")


@dbc.command(short_help="See the API docs and introductory tutorial.")
def docs():
    """Display the API docs and introductory tutorial in the browser,
    using the packaged HTML doc files."""
    html_path = str((Path(__file__).parent.parent / "html" / "index.html").resolve())
    index_path = f"file://{html_path}"
    click.echo(f"Opening {index_path}")
    webbrowser.open(index_path)


@dbc.command()
@click.option(
    "--profiles-dir", envvar="DBC_PROFILES_DIR", default="./dbc", required=False
)
@click.option(
    "--project-dir", envvar="DBC_PROJECT_DIR", default="./dbc/jobs", required=False
)
@click.option("--job", default=None, help="Job to be run", required=False)
def run(profiles_dir, project_dir, job):
    dir = here
    if Path(project_dir).is_dir():
        dir = project_dir
    else:
        dir = os.path.join(here, project_dir)

    if job:  # run single job
        source = os.path.join(dir, job)
        click.echo(f"run job: {source}")
        run_job(source, profiles_dir)
    else:  # run all jobs in jobs directory
        click.echo(f"run all jobs in directory: {dir}")
        run_all_job_in_directory(dir, profiles_dir)


def main():
    dbc()


if __name__ == "__main__":
    main()
