import importlib

import typer
from dagster_cloud_cli.utils import create_stub_app

from .commands.branch_deployment import app as branch_deployment_app
from .commands.config import app as config_app
from .commands.config import app_configure as configure_app
from .commands.deployment import app as deployment_app
from .commands.job import app as job_app
from .commands.organization import app as organization_app
from .commands.organization import legacy_settings_app
from .commands.run import app as run_app
from .commands.sandbox import app as sandbox_app
from .commands.serverless import app as serverless_app
from .commands.workspace import app as workspace_app
from .version import __version__

has_dagster_cloud = importlib.util.find_spec("dagster_cloud") is not None


if has_dagster_cloud:
    from dagster_cloud.agent.cli import app as agent_app
    from dagster_cloud.pex.grpc.server.cli import app as pex_app
else:
    agent_app = create_stub_app("dagster-cloud")
    pex_app = create_stub_app("dagster-cloud")


def _import_commands(parent: typer.Typer, child: typer.Typer) -> None:
    """
    Copies the commands from one Typer app to another.
    Equivalent of `add_typer` but doesn't add a subcommand.
    """
    for command in child.registered_commands:
        parent.registered_commands.append(command)


app = typer.Typer(
    help="CLI tools for working with Dagster Cloud.",
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"],
    },
)


def version_callback(value: bool):
    if value:
        typer.echo(f"Dagster Cloud version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    _version: bool = typer.Option(
        False,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        show_default=False,
        help="Show Dagster Cloud version.",
    )
):
    return


app.add_typer(agent_app, name="agent", no_args_is_help=True)
app.add_typer(config_app, name="config", no_args_is_help=True)
app.add_typer(deployment_app, name="deployment", no_args_is_help=True)
app.add_typer(organization_app, name="organization", no_args_is_help=True)
app.add_typer(workspace_app, name="workspace", no_args_is_help=True)
app.add_typer(sandbox_app, name="sandbox", no_args_is_help=True, hidden=True)
app.add_typer(branch_deployment_app, name="branch-deployment", no_args_is_help=True)
app.add_typer(job_app, name="job", no_args_is_help=True)
app.add_typer(run_app, name="run", no_args_is_help=True, hidden=True)
app.add_typer(serverless_app, name="serverless", no_args_is_help=True)
app.add_typer(pex_app, name="pex", hidden=True, no_args_is_help=True)


# Deprecated in favor of organization
app.add_typer(legacy_settings_app, name="settings", hidden=True)

_import_commands(app, configure_app)

if __name__ == "__main__":
    app()
