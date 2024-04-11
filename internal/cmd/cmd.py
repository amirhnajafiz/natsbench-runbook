import subprocess


"""run command executes a nats bench command.

params:
    - command: string

returns:
    - string
"""
def run(command: str) -> tuple[str, str]:
    # split command to an array
    subcommands = command.split(" ")
    
    # execute the command using subprocess
    out = subprocess.run(["nats", "bench", subcommands], stdout=subprocess.PIPE, text=True)
    if out.returncode != 0:
        return out.stderr, "failed to execute give command"
    
    return out.stdout, ""
    