import argparse
import logging
import tarfile
import json
import os

from pathlib import Path, PosixPath
from datetime import datetime, timezone

from visionaire4 import configs

IMPORT_TYPE = [
    "metrics",
    "edge"
]
logger = logging.getLogger()


def extract_snapshot(filepath: str, out_dir: str) -> str:
    out_dir: PosixPath = Path(out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    with tarfile.open(filepath, mode="r") as tar:
        tar.extractall(out_dir)
    p = Path(filepath)
    suffix = "".join(p.suffixes)
    dir_name = p.name.replace(suffix, "")
    return out_dir.joinpath(dir_name)


def get_snapshot_interval(snapshot_path):
    snapshot_path = Path(snapshot_path)
    valid = False
    meta_path = ""
    for item in snapshot_path.iterdir():
        if item.is_file():
            continue
        meta_path = item.joinpath("meta.json")
        if meta_path.exists():
            valid = True
            break
    if not valid:
        return "", ""

    with meta_path.open('r') as f:
        metadata = json.load(f)
    date_from = datetime.fromtimestamp(metadata['minTime']//1000, timezone.utc)
    date_from = date_from.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_to = datetime.fromtimestamp(metadata['maxTime']//1000, timezone.utc)
    date_to = date_to.strftime("%Y-%m-%dT%H:%M:%SZ")
    return date_from, date_to

def import_metrics(args):
    cfg_dir: PosixPath = Path(args.cfg_dir).expanduser().resolve()
    if cfg_dir.is_file():
        raise RuntimeError(f"Config directory (--cfg-dir) '{args.cfg_dir}' is file, "
            "expected to be a directory.")
    cfg_dir.mkdir(parents=True, exist_ok=True)

    compose_cmd = configs.docker_compose_cmd()
    compose_dir = cfg_dir.joinpath("compose")
    compose_path = compose_dir.joinpath("docker-compose.yml")
    if args.down:
        logger.info("Stopping docker compose")
        success = configs.compose_down(compose_dir, compose_cmd)
        if not success:
            raise RuntimeError("Failed when stopping docker compose. Something is wrong.")
        logger.info("Successfully stopping docker compose")
        return
    if args.file == "":
        raise RuntimeError("Argument '--file' or '-f' is required when importing data.")
    if not Path(args.file).exists():
        raise FileNotFoundError(f"Exported file (--file) in {args.file} is not found.")

    snapshot_dir = cfg_dir.joinpath("snapshot")
    logger.debug(f"Extracting exported data {args.file} to {snapshot_dir}")
    snapshot_path = extract_snapshot(args.file, snapshot_dir)
    time_from, time_to = get_snapshot_interval(snapshot_path)
    if time_from == "" or time_to == "":
        raise RuntimeError(f"The specified file '{args.file}' has an invalid format.")
    logger.debug(f"File exported to {snapshot_path}")

    uid = os.environ.get("UID", 1000)

    dashboard_dir = cfg_dir.joinpath("dashboards")
    dashboard_cfg_path = dashboard_dir.joinpath("dashboards.yml")
    datasource_dir = cfg_dir.joinpath("datasources")
    datasource_cfg_path = datasource_dir.joinpath("datasources.yml")
    configs.gen_compose_config(compose_path, dashboard_dir, datasource_dir, snapshot_path, uid)
    configs.gen_grafana_dashboard_cfg(dashboard_cfg_path)
    configs.gen_grafana_datasource_cfg(datasource_cfg_path)
    configs.gen_grafana_dashboards(dashboard_dir, time_from, time_to)

    logger.info("Running monitoring servers.")
    success = configs.compose_up(compose_dir, compose_cmd)
    if not success:
        raise RuntimeError("Failed when running monitoring servers. Something is wrong.")
    logger.info("Successfully running monitoring servers.")

    compose_cmd_txt = " ".join(compose_cmd)
    cmd_msg = f"visionaire4 import metrics -d {str(cfg_dir)} --down"
    logger.info(f"You can stop monitoring server with '{compose_cmd_txt} down' in {str(compose_dir)}, "
        f"or by running '{cmd_msg}'")
    logger.info("Monitoring servers available at http://localhost:3000 with user 'admin' and password 'admin'")


def main(args):
    msg_type = "edge cases" if args.type == "edge" else args.type
    logger.info(f"Start importing Visionaire4 {msg_type} data.")

    if args.type == "metrics":
        import_metrics(args)
    else:
        raise RuntimeError("edges cases import is not yet implemented.")


def add_parser(subparser, parent_parser=None):
    parent_parser = [parent_parser] or []
    BENCH_HELP = "Import Visionaire4 data (metrics, edge cases) to host"
    parser: argparse.ArgumentParser = subparser.add_parser(
        "import",
        parents=parent_parser,
        help=BENCH_HELP, description=BENCH_HELP,
        usage="\n  visionaire4 import TYPE [options]"
    )

    parser.add_argument(
        "type", type=str, metavar="TYPE",
        help="type of data to import, choice: [{}]".format(
            ", ".join(IMPORT_TYPE)),
        choices=IMPORT_TYPE
    )
    parser.add_argument(
        "--file", "-f",
        type=str, default="",
        help="Path to exported file to be imported."
    )
    parser.add_argument("--down", action="store_true", help="stop docker compose")
    parser.add_argument(
        "--cfg-dir", "-d",
        type=str, default="~/nodeflux/import", metavar="DIR",
        help="Export file output directory. Default: '~/nodeflux/import'"
    )
    parser.set_defaults(func=main)
