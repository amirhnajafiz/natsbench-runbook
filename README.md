# Cronjob Charts

Helm chart for creating your cronjobs in ```kubernetes``` cluster. By using this
chart you can manage your cronjobs by editing only one file. This chart will reduce
your time to set or edit your cronjobs. It also gives you a versioning ability on your
cronjobs.

## values

In ```values.yml``` file you can set your cronjobs based on the following structure:

```yaml
jobs:
  - name: job-name
    version: v0.1.1
    cron: '1 * * * * *'
    restartPolicy: never
    spec:
      container:
        image: container-name
        tag: v0.1.0
        command: ['ls', '-la']
```
