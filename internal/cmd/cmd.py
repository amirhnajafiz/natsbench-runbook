import subprocess


"""bench command executes a nats bench command.

params:
    - command: string
    - path: string
    - timeout_s: int

returns:
    - tuple: (string, boolean)
"""
def bench(command: str, path: str, timeout_s: int) -> tuple[str, bool]:
    # split command to an array
    subcommands = command.split(" ")
    command_list = ["nats", "bench", "--no-progress", f'--csv={path}'] + subcommands
    
    # running bench as a syscall
    return syscall(command_list, timeout_s=timeout_s)


"""syscall is used to execute a normal command, not a bench command.

params:
    - command: string

returns:
    - tuple: (string, boolean)
"""
def syscall(command: str, timeout_s: int = 180) -> tuple[str, bool]:
    # split command to an array
    command_list = command.split(" ")
    
    try:
        # execute the command using subprocess
        out = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout_s)
        if out.returncode != 0:
            return out.stderr, True
        
        return out.stdout, False
    except subprocess.TimeoutExpired:
        return f"command hit {timeout_s} seconds timeout!", True
