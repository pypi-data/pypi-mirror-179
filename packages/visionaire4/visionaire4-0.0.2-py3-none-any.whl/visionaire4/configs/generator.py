import yaml
import json

from pathlib import Path, PosixPath

from .compose import PROM_COMPOSE, compose_up, compose_down, docker_compose_cmd
from .configs import GRAFANA_DASHBOARD, GRAFANA_DATASOURCE
from .visionaire4_dashboard import VISIONAIRE4_DASHBOARD
from .resource_dashboard import RESOURCE_DASHBOARD
from .hybrid_dashboard import HYBRID_DASHBOARD


def _dump_yaml(filepath, data):
    filepath: PosixPath = Path(filepath).expanduser()
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open("w") as f:
        yaml.dump(data, f, sort_keys=False)
    return str(filepath)


def _change_path(data: str, change_to: str):
    path = data.split(':')
    path[0] = str(Path(change_to).expanduser())
    data = ":".join(path)
    return data


def _dump_dashboard(filepath, data, time_from, time_to):
    dashboard = json.loads(data)
    dashboard['time']['from'] = time_from
    dashboard['time']['to'] = time_to
    dashboard['refresh'] = ""

    filepath: PosixPath = Path(filepath).expanduser()
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open("w") as f:
        json.dump(dashboard, f, indent=2)


def gen_compose_config(filepath, dashboard_dir, datasource_dir, snapshot_dir, uid):
    compose_cfg = yaml.safe_load(PROM_COMPOSE)
    compose_cfg['services']['prometheus']['volumes'][0] = _change_path(
        compose_cfg['services']['prometheus']['volumes'][0], snapshot_dir)
    compose_cfg['services']['grafana']['volumes'][0] = _change_path(
        compose_cfg['services']['grafana']['volumes'][0], dashboard_dir)
    compose_cfg['services']['grafana']['volumes'][1] = _change_path(
        compose_cfg['services']['grafana']['volumes'][1], datasource_dir)
    compose_cfg['services']['prometheus']['user'] = f"{uid}:{uid}"
    _dump_yaml(filepath, compose_cfg)


def gen_grafana_dashboard_cfg(filepath):
    dashboard_cfg = yaml.safe_load(GRAFANA_DASHBOARD)
    _dump_yaml(filepath, dashboard_cfg)


def gen_grafana_datasource_cfg(filepath):
    datasource_cfg = yaml.safe_load(GRAFANA_DATASOURCE)
    _dump_yaml(filepath, datasource_cfg)


def gen_grafana_dashboards(output_dir, time_from, time_to):
    output_dir = Path(output_dir)
    _dump_dashboard(output_dir.joinpath("visionaire4.json"), VISIONAIRE4_DASHBOARD, time_from, time_to)
    _dump_dashboard(output_dir.joinpath("resources.json"), RESOURCE_DASHBOARD, time_from, time_to)
    _dump_dashboard(output_dir.joinpath("hybrid.json"), HYBRID_DASHBOARD, time_from, time_to)
