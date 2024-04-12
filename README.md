# NATS Bench Runbook

This is a runbook for automating nats-bench commands. It uses nats-cli bench feature in order to execute bench commands.

## Config

Copy the example ```cmd.example.json``` file in **config** directory into ```cmd.json``` in root directory.After that you can change the commands in that json file. After running ```python3 main.py``` command, it will read your commands from ```cmd.json``` file and exports the results into ```tmp``` directory.

A complete section of a command is represented below. Each command has a ```name``` lable. The ```count``` label is used when you want to repeat a command multiple times. ```command``` field is where you put nats-bench attributes (please don't as ```--csv``` and ```--no-progress``` commands since the runbook sets them). The ```pre-commands``` fields is an array of commands that you want to run before bench process. If you set ```syscall``` label, you can run any shell commands instead of nats-bench commands.

```json
{
    "name": "normal-stats",
    "count": 20,
    "command": "rides --pub 5 --sub 15 -s nats://0.0.0.0:4222",
    "pre-commands": [
        "nats stream delete benchstream --force -s nats://0.0.0.0:4222"
    ],
    "syscall": false
}
```

## Hypothesis testing

A good feature in this runbook is hypothesis testing of a config change in nats-server. After you benchmakr the cluster, you can compare your changes by running ```python3 htest.py``` command. This script gets two input argument which are the directory names in ```tmp``` directory (referred as groups). After that, it will run a hypothesis test to compare read, write, and overall stats between those groups.
