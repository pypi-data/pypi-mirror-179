
GRAFANA_DATASOURCE = \
"""
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    orgId: 1
    url: http://prometheus:9090
    basicAuth: false
    isDefault: true
    editable: true
"""

GRAFANA_DASHBOARD = \
"""
apiVersion: 1

providers:
  - name: 'dashboards'
    orgId: 1
    folder: 'Visionaire4'
    type: file
    disableDeletion: false
    updateIntervalSeconds: 60
    allowUiUpdates: true
    options:
      path: /etc/grafana/provisioning/dashboards
"""
