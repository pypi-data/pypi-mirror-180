from os import system as run, path as ospath
from pathlib import Path
from rich.panel import Panel
from rich.table import Table
from rich import print
from rich.console import Console
from typing import List, Optional

err_console = Console(stderr=True)

from compose_companion.configurations import Configurations


def container_up(container: str, recreate: bool, build: bool):
    scripts = Configurations().scripts
    compose_file = Configurations().compose_file

    if scripts.get("x-before-up", {}).get(container):
        for script in scripts["x-before-up"]["before-each"]:
            run(script)
        for script in scripts["x-before-up"][container]:
            run(script)

    run(
        f"docker compose -f {compose_file} up -d --remove-orphans {container} --force-recreate={recreate} --build={build}"
    )

    if scripts.get("x-after-up", {}).get(container):
        for script in scripts["x-after-up"]["after-each"]:
            run(script)
        for script in scripts["x-after-up"][container]:
            run(script)


def container_down(container: str, volumes: bool):
    scripts = Configurations().scripts
    compose_file = Configurations().compose_file

    if scripts.get("x-before-down", {}).get(container):
        for script in scripts["x-before-down"][container]:
            run(script)

    run(f"docker compose -f {compose_file} rm -sf -v={volumes} {container}")

    if scripts.get("x-after-down", {}).get(container):
        for script in scripts["x-after-down"][container]:
            run(script)


def container_create(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} create {container}")


def container_stop(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} stop {container}")


def container_pause(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} pause {container}")


def container_unpause(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} unpause {container}")


def container_start(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} start {container}")

def backup_volumes(container: str, volumes: Optional[List[str]], backup_dir: Optional[str]):
    conf_volumes = Configurations().volumes[container]

    if backup_dir:
        path_backup_dir = Path(ospath.expandvars(backup_dir.replace('~', '$HOME'))).resolve()
        if path_backup_dir.is_file():
            err_console.print("This path refers to an existing file, please pass a directory.")
            return
        path_backup_dir.mkdir(parents=True, exist_ok=True)
        back_dir = path_backup_dir
    else:
        Path('./compose-backup').resolve().mkdir(parents=True, exist_ok=True)
        back_dir = Path('./compose-backup').resolve()

    for volume in conf_volumes:
        was_picked = volume['host'] in volumes if volumes else True

        if was_picked:
            run(f"docker run --rm --volumes-from {container} -v {back_dir}:/backup ubuntu tar cvf /backup/{volume['host']}.tar {volume['container']}")
            if volumes:
                volumes.remove(volume['host'])

    for remaining in volumes:
        err_console.print(f"Volume {remaining} not declared. Skipping...")

def restore_volumes(container: str, volumes: Optional[List[str]], backup_dir: Optional[str]):
    conf_volumes = Configurations().volumes[container]

    if backup_dir:
        path_backup_dir = Path(ospath.expandvars(backup_dir.replace('~', '$HOME'))).resolve()
        if not path_backup_dir.is_dir():
            err_console.print("The given path does not exist or is not a directory.")
            return
        back_dir = path_backup_dir
    else:
        back_dir = Path('./compose-backup').resolve()
    
    for volume in conf_volumes:
        was_picked = volume['host'] in volumes if volumes else True
        backup_exists = Path(f"{back_dir}/{volume['host']}.tar").resolve().is_file()

        if was_picked and backup_exists:
            run(f"docker run --rm --volumes-from {container} -v {back_dir}:/backup ubuntu bash -c \"cd /{volume['container']} && tar xvf /backup/{volume['host']}.tar --strip 1\"")
            if volumes:
                volumes.remove(volume['host'])
        elif was_picked:
            err_console.print(f"No backup found for {volume['host']}. Skiping...")

    for remaining in volumes:
        print(err_console.print(f"Volume {remaining} not declared. Skipping..."))

def print_config():
    [config_keys, get_config] = [
        Configurations().config_keys,
        Configurations().get_config,
    ]

    grid = Table.grid(expand=True)
    grid.add_column("Key", style="cyan")
    grid.add_column("Value", style="magenta")
    for key in config_keys:
        grid.add_row(
            key,
            get_config(key),
        )

    panel = Panel(
        grid,
        title="Configurations",
        title_align="left",
        border_style="dim",
    )

    print(panel)
