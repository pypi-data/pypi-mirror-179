import subprocess

from typing import List

PROM_COMPOSE = \
r"""
version: '2.1'

networks:
  monitor-net:
    driver: bridge

services:
  prometheus:
    image: prom/prometheus:v2.40.0
    container_name: prometheus
    user: "uid:uid"
    volumes:
      - snapshot_dir:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    restart: unless-stopped
    expose:
      - 9090
    ports:
      - "9090:9090"
    networks:
      - monitor-net
    labels:
      org.label-schema.group: "monitoring"

  grafana:
    image: grafana/grafana:9.2.4
    container_name: grafana
    volumes:
      - dashboard_path:/etc/grafana/provisioning/dashboards
      - datasource_path:/etc/grafana/provisioning/datasources
    environment:
      - GF_SECURITY_ADMIN_USER=${ADMIN_USER:-admin}
      - GF_SECURITY_ADMIN_PASSWORD=${ADMIN_PASSWORD:-admin}
      - GF_USERS_ALLOW_SIGN_UP=false
    restart: unless-stopped
    expose:
      - 3000
    ports:
      - "3000:3000"
    networks:
      - monitor-net
    labels:
      org.label-schema.group: "monitoring"
"""


def docker_compose_cmd() -> List[str]:
    ret = subprocess.run(["docker", "compose", "version"], capture_output=True)
    if ret.returncode == 0:
        return ["docker", "compose"]
    ret = subprocess.run(["docker-compose", "version"], capture_output=True)
    if ret.returncode == 0:
        return ["docker-compose"]
    raise RuntimeError("Could not find docker compose installation, follow this "
        "installation process https://docs.docker.com/compose/install/linux/")


def run_command(command, cwd):
    command = " ".join(command)
    ret = subprocess.run(command, cwd=cwd, shell=True, universal_newlines=True)
    return ret.returncode


def compose_up(working_dir: str, compose_cmd: List[str]) -> bool:
    compose_cmd.extend(["up", "-d"])
    ret = run_command(compose_cmd, working_dir)
    if ret != 0:
        return False
    return True


def compose_down(working_dir: str, compose_cmd: List[str]) -> bool:
    compose_cmd.extend(["down"])
    ret = run_command(compose_cmd, working_dir)
    if ret != 0:
        return False
    return True
