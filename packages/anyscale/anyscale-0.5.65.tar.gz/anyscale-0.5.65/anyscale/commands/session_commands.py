import os
from typing import Any, Optional, Tuple

import click

from anyscale.cli_logger import BlockLogger
from anyscale.controllers.project_controller import COMPUTE_CONFIG_FILENAME
from anyscale.controllers.session_controller import SessionController


log = BlockLogger()


@click.command(name="down", help="[DEPRECATED] Stop the current cluster.", hidden=True)
@click.argument("session-name", required=False, default=None)
@click.option(
    "--workers-only", is_flag=True, default=False, help="Only destroy the workers."
)
@click.option(
    "--keep-min-workers",
    is_flag=True,
    default=False,
    help="Retain the minimal amount of workers specified in the config.",
)
@click.option("--delete", help="Delete the cluster as well.", is_flag=True)
@click.option(
    "--skip-snapshot",
    help="DEPRECATED. Skip taking a snapshot.",
    is_flag=True,
    default=True,
)
@click.pass_context
def anyscale_stop(
    ctx: Any,
    session_name: Optional[str],
    workers_only: bool,
    keep_min_workers: bool,
    delete: bool,
    skip_snapshot: bool,
) -> None:
    log.warning(
        "`anyscale down` has been deprecated. Please use `anyscale cluster terminate` instead."
    )
    if skip_snapshot:
        log.warning(
            "`skip_snapshot` has been deprecated. Snapshots are no longer taken during cluster termination."
        )
    session_controller = SessionController()
    session_controller.stop(
        session_name,
        workers_only=workers_only,
        keep_min_workers=keep_min_workers,
        delete=delete,
    )


@click.command(
    name="start",
    context_settings=dict(ignore_unknown_options=True,),
    help="[DEPRECATED] Start or update a cluster based on the current project configuration.",
    hidden=True,
)
@click.argument("session-name", required=False)
@click.option(
    "--build-id",
    help=(
        "The build ID generated from the app templates service. Either the --build-id "
        "or the --build-identifier must be specified."
    ),
    # TODO: add the app templates CLI command to the description
    # once the CLI is done.
    default=None,
    required=False,
)
@click.option(
    "--build-identifier",
    help=(
        "The build identifier for a build generated from the app config service. "
        "A build identifier consists of an app config name and an optional revision "
        "of the build. Eg: 'my_app_config:2' where 2 is the revision number. If no "
        "revision is specified, use the latest revision. Either the --build-id or the "
        "--build-identifier must be specified."
    ),
    default=None,
    required=False,
)
@click.option(
    "--compute-config",
    help=(
        "The JSON file of the compute config to launch this cluster with. "
        "An example can be found at {filename}. "
        "The full JSON schema can be viewed at {website}. ".format(
            filename=COMPUTE_CONFIG_FILENAME, website="api.anyscale.com/v0/docs",
        )
    ),
    required=True,
)
@click.option(
    "--idle-timeout",
    required=False,
    help="Idle timeout (in minutes), after which the cluster is stopped. Idle "
    "time is defined as the time during which a cluster is not running a user "
    "command (through 'anyscale exec' or the Web UI), and does not have an "
    "attached driver. Time spent running Jupyter commands, or commands run "
    "through ssh, is still considered 'idle'. -1 means no timeout. "
    "Default: 120 minutes",
    type=int,
)
@click.option(
    "--sync-files",
    is_flag=True,
    default=False,
    help=("Syncs working directory after the session is started"),
    hidden=True,
)
def anyscale_start(
    session_name: Optional[str],
    build_id: str,
    build_identifier: str,
    compute_config: str,
    idle_timeout: Optional[int],
    sync_files: bool,
) -> None:
    log.warning(
        "`anyscale start` has been deprecated. Please use `anyscale cluster start` instead."
    )
    session_controller = SessionController()
    session_controller.start(
        session_name=session_name,
        compute_config=compute_config,
        build_id=build_id,
        build_identifier=build_identifier,
        idle_timeout=idle_timeout,
        sync_files=sync_files,
    )


@click.command(name="ssh", help="SSH into head node of cluster.", hidden=True)
@click.argument(
    "cluster-name", type=str, required=False, default=None, envvar="CLUSTER_NAME"
)
@click.option("-o", "--ssh-option", multiple=True)
@click.option(
    "-w",
    "--worker-node-id",
    type=str,
    default=None,
    help=(
        "SSH into the given worker node id instead of the head node. "
        "You can also run this command directly on the head node. "
        "ssh_options are ignored when SSHing from the head node "
        "to the worker node."
    ),
)
@click.option(
    "-n",
    "--worker-node-ip",
    type=str,
    default=None,
    help=(
        "SSH into the given worker node ip address instead of the head node. "
        "You can also run this command directly on the head node. "
        "ssh_options are ignored when SSHing from the head node "
        "to the worker node."
    ),
)
@click.option(
    "-h",
    "--force-head-node",
    type=bool,
    default=False,
    hidden=True,
    help=(
        "Force the ssh to the worker node id to assume it's on the "
        "head node when we know it's supposed to be there."
    ),
)
@click.option(
    "--project-id",
    required=False,
    default=None,
    help=(
        "Override project id used for this cluster. If not provided, the Anyscale project "
        "context will be used if it exists. Otherwise a default project will be used."
    ),
)
def anyscale_ssh(
    cluster_name: str,
    ssh_option: Tuple[str],
    worker_node_id: Optional[str],
    worker_node_ip: Optional[str],
    force_head_node: bool,
    project_id: Optional[str],
) -> None:
    if not cluster_name:
        cluster_name = os.getenv("SESSION_NAME", "")

    session_controller = SessionController()
    session_controller.ssh(
        cluster_name,
        ssh_option,
        worker_node_id,
        worker_node_ip,
        force_head_node,
        project_id,
    )


@click.command(
    name="push", help="DEPRECATED: Push current project to cluster.", hidden=True
)
@click.argument(
    "session-name", type=str, required=False, default=None, envvar="SESSION_NAME"
)
@click.option(
    "--source",
    "-s",
    type=str,
    required=False,
    default=None,
    help="Source location of the files on the local file system which should"
    "be transferred. If source and target are specified, only those files/directories "
    "will be updated.",
)
@click.option(
    "--target",
    "-t",
    type=str,
    required=False,
    default=None,
    help="Target location on the head node to transfer the files to. If source "
    "and target are specified, only those files/directories will be updated.",
)
@click.option(
    "--config",
    type=str,
    required=False,
    default=None,
    help="Updates session with this configuration file.",
)
@click.option(
    "--all-nodes",
    "-A",
    is_flag=True,
    required=False,
    help="[DEPRECATED] Choose to update to all nodes (workers and head) if source and target are specified.",
)
@click.pass_context
def anyscale_push(
    ctx: Any,
    session_name: str,
    source: Optional[str],
    target: Optional[str],
    config: Optional[str],
    all_nodes: bool,
) -> None:
    session_controller = SessionController()
    session_controller.push(session_name, source, target, config, all_nodes)


@click.command(name="pull", help="DEPRECATED: Pull cluster", hidden=True)
@click.argument(
    "session-name", type=str, required=False, default=None, envvar="SESSION_NAME"
)
@click.option(
    "--source",
    "-s",
    type=str,
    required=False,
    default=None,
    help="Source location to transfer files located on head node of cluster "
    "from. If source and target are specified, only those files/directories "
    "will be updated.",
)
@click.option(
    "--target",
    "-t",
    type=str,
    required=False,
    default=None,
    help="Local target location to transfer files to. If source and target "
    "are specified, only those files/directories will be updated.",
)
@click.option(
    "--config",
    type=str,
    required=False,
    default=None,
    help="Pulls cluster configuration from cluster this location.",
)
@click.confirmation_option(
    prompt="Pulling a cluster will override the local project directory. Do you want to continue?"
)
def anyscale_pull(
    session_name: str,
    source: Optional[str],
    target: Optional[str],
    config: Optional[str],
) -> None:
    session_controller = SessionController()
    session_controller.pull(session_name, source, target, config)
