import subprocess


"""run command executes a nats bench command.

params:
    - command: string

returns:
    - tuple: (string, boolean)
"""
def run(command: str, path: str) -> tuple[str, bool]:
    # split command to an array
    subcommands = command.split(" ")
    command_list = ["nats", "bench", f'--csv={path}'] + subcommands
    
    # execute the command using subprocess
    out = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if out.returncode != 0:
        return out.stderr, True
    
    return out.stdout, False
    