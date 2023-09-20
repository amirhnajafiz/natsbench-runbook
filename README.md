# Cronjob Charts

![GitHub release (with filter)](https://img.shields.io/github/v/release/amirhnajafiz/cronjob-charts)
![GitHub top language](https://img.shields.io/github/languages/top/amirhnajafiz/cronjob-charts)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amirhnajafiz/cronjob-charts)

Helm chart for creating your cronjobs in ```kubernetes``` cluster. By using this
chart you can manage your cronjobs by editing only one file. This chart will reduce
your time to set or edit your cronjobs. It also gives you a versioning ability on your
cronjobs.

## :ticket: values

In ```values.yml``` file you can set your cronjobs based on the following structure:

```yaml
jobs:
  - name: pull-codes
    cron: "* 1 * * * *"
    image: amirhossein21/gitPuller:v0.1.0
    env:
    - name: REPO
      valueFrom:
        configMapKeyRef:
          name: pull-codes-configmap
          key: repository.path
```

## :wrench: configs

In order to manage cronjobs global configs you can change the following section
in ```values.yaml``` file.

```yaml
config:
  restartPolicy: Never # containers restart policy
  imagePullPolicy: IfNotPresent # image pulling policy
```

## :rocket: install

After you make your changes, use the following command in order to release the charts
on your cluster.

```shell
helm install cronjobs cronjobs
```

## :pushpin: usage

Imagine you have ```staging``` and ```production``` namespaces and you want to create
3 cronjobs for logs exporting, metrics exporting, and garbage collecting in your database.
You need to build 6 manifests in order to do that. But by using ```cronjob charts``` you
can create only 3 ```values.yaml``` files and create your jobs there.

### values.yaml

First create a base ```values.yaml``` file to create your jobs.

```yaml
service: # service type can only be ClusterIP
  type: ClusterIP

ingress: # ingress should be disabled
  enable: false

config: # containers configs
  restartPolicy: Never
  imagePullPolicy: IfNotPresent
```

### values.staging.yaml

The create a file for staging namespace (it will override the ```values.yaml```):

```yaml
jobs:
  - name: logs-exporter
    cron: "* 1 * * * *"
    image: elasticsearch-filebeat:v2.96.1
    env:
    - name: HOST
      value: elasticsearch.elasticsearch:9290
    - name: LOG_FILE
      valueFrom:
        configMapKeyRef:
          name: elk-config
          key: logs.path
  - name: metrics-exporter
    cron: "* 1 * * * *"
    image: prometheus:go-v0.1.46
    env:
    - name: TARGET
      valueFrom:
        configMapKeyRef:
          name: metrics-config
          key: host
  - name: collector
    cron: "1 * * * * *"
    image: amirhossein21/collector:v0.2.0
    env:
    - name: HOST
      value: snappline.mariadb.staging.default:6033
```

```shell
helm install cronjobs cronjobs -f values.staging.yaml
```

### values.production.yaml

The create a file for production namespace (it will override the ```values.yaml```):

```yaml
jobs:
  - name: logs-exporter
    cron: "* 5 1 * * *"
    image: elasticsearch-filebeat:v2.96.1
    env:
    - name: HOST
      value: elasticsearch.elasticsearch:9290
    - name: LOG_FILE
      valueFrom:
        configMapKeyRef:
          name: elk-config
          key: logs.path
  - name: metrics-exporter
    cron: "* 1/5 * * * *"
    image: prometheus:go-v0.1.46
    env:
    - name: TARGET
      valueFrom:
        configMapKeyRef:
          name: metrics-config
          key: host
  - name: collector
    cron: "* * 1 * * *"
    image: amirhossein21/collector:v1.2.0
    env:
    - name: HOST
      value: snappline.mariadb.production.default:6033
```

```shell
helm install cronjobs cronjobs -f values.production.yaml
```
