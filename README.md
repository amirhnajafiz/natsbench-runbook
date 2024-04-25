# NATS Bench Runbook

This is a runbook for automating nats-bench commands. It uses nats-cli bench feature in order to execute bench commands.

## Config

Copy the example ```cmd.example.json``` file in **config** directory into ```cmd.json``` in root directory.After that you can change the commands in that json file. After running ```python3 main.py``` command, it will read your commands from ```cmd.json``` file and exports the results into ```tmp``` directory.

A complete section of a command is represented below. Each command has a ```name``` lable. The ```count``` label is used when you want to repeat a command multiple times. ```command``` field is where you put nats-bench attributes (please don't as ```--csv``` and ```--no-progress``` commands since the runbook sets them). The ```pre-commands``` fields is an array of commands that you want to run before bench process. If you set ```syscall``` label, you can run any shell commands instead of nats-bench commands.

```json
[
    {
        "name": "context-switch",
        "command": "nats context select default",
        "syscall": true
    },
    {
        "name": "normal-stats",
        "count": 5,
        "command": "rides --pub 5 --sub 15",
        "pre-commands": [
            "nats stream delete benchstream --force"
        ],
        "syscall": false
    }
]
```

### context config

```json
{
  "description": "",
  "url": "nats://172.21.88.124:4222",
  "socks_proxy": "",
  "token": "",
  "user": "",
  "password": "",
  "creds": "",
  "nkey": "",
  "cert": "",
  "key": "",
  "ca": "",
  "nsc": "",
  "jetstream_domain": "",
  "jetstream_api_prefix": "",
  "jetstream_event_prefix": "",
  "inbox_prefix": "",
  "user_jwt": "",
  "color_scheme": ""
}
```

## Hypothesis testing

A good feature in this runbook is hypothesis testing of a config change in nats-server. After you benchmakr the cluster, you can compare your changes by running ```python3 htest.py``` command. This script gets two input argument which are the directory names in ```tmp``` directory (referred as groups). After that, it will run a hypothesis test to compare read, write, and overall stats between those groups.

## Build and run

```sh
docker build . -f build/Dockerfile -t amirhossein21/natsbench-runbook:v0.0.4
docker run -v ./tmp:/usr/src/app/tmp -v ./cmd.json:/usr/src/app/cmd.json -v ./default.json:/root/.config/nats/context/js-p.json amirhossein21/natsbench-runbook:v0.0.4 nats context ls
```
