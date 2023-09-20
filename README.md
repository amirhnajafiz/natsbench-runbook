# Cronjob Charts

![GitHub release (with filter)](https://img.shields.io/github/v/release/amirhnajafiz/cronjob-charts)
![GitHub top language](https://img.shields.io/github/languages/top/amirhnajafiz/cronjob-charts)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amirhnajafiz/cronjob-charts)

Helm chart for creating your cronjobs in ```kubernetes``` cluster. By using this
chart you can manage your cronjobs by editing only one file. This chart will reduce
your time to set or edit your cronjobs. It also gives you a versioning ability on your
cronjobs.

## values

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

## configs

In order to manage cronjobs global configs you can change the following section
in ```values.yaml``` file.

```yaml
config:
  restartPolicy: Never # containers restart policy
  imagePullPolicy: IfNotPresent # image pulling policy
```

## install

After you make your changes, use the following command in order to release the charts
on your cluster.

```shell
helm install cronjobs cronjobs
```
