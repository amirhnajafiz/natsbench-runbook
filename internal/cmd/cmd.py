import subprocess


"""run command executes a nats bench command.

params:
    - command: string
    - path: string

returns:
    - tuple: (string, boolean)
"""
def run(command: str, path: str) -> tuple[str, bool]:
    # split command to an array
    subcommands = command.split(" ")
    command_list = ["nats", "bench", "--no-progress", f'--csv={path}'] + subcommands
    
    # execute the command using subprocess
    out = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if out.returncode != 0:
        return out.stderr, True
    
    return out.stdout, False


"""syscall is used to execute a normal command, not a bench command.

params:
    - command: string

returns:
    - tuple: (string, boolean)
"""
def syscall(command: str) -> tuple[str, bool]:
    # split command to an array
    command_list = command.split(" ")
    
    # execute the command using subprocess
    out = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if out.returncode != 0:
        return out.stderr, True
    
    return out.stdout, False
