from system.error import panic
import system.msg as es
from internal.config import exists
from internal.config.config import load
from internal.cmd.cmd import run, syscall
from internal.exporter import make
from internal.exporter.csv import export_dataset
import internal.exporter.writer as writer
from internal.exporter.gc import cleanup
from internal.parser.parser import raw_parsing
from internal.parser.dataset import create_dataset


"""handle syscall is used to execute a system-call.

params:
    - command: string
"""
def handle_syscall(command: str, notify: bool=False):
    # execute system-call
    out, err = syscall(command=command)
    if notify:
        print(out)
    if err and notify: # check for errors
        print(es.ERR_EXEC_COMMAND)


"""handle command is used to execute a command.

params:
    - command: dictionary
"""
def handle_command(command: dict) -> str:
    # reserve the output dir
    location = writer.new_command(command["name"])
    # set bound limit
    bound = int(command["count"])+1

    # loop on the count of each command
    for index in range(1, bound): 
        # execute a command's pre-commands
        for precommand in command["pre-commands"]:
            handle_syscall(precommand)
        
        # execute the command
        raw, err = run(command["command"], f'{location}/xcmd-{index}.csv')
        if err: # check for errors
            print(raw)
            print(es.ERR_EXEC_COMMAND)
            continue
        
        # parse the raw output
        out = raw_parsing(raw.strip())
        
        # export outputs
        writer.export(raw, f'{location}/xcmd-{index}.raw')
        writer.export(out, f'{location}/xcmd-{index}.out')
    
    # create the result dataset and save it
    ds = create_dataset(location)
    export_dataset(f'{location}/dataset.csv', ds)
    
    return location


"""main function of nats-bench runbook.
"""
def main():
    if not exists(): # check the cmd.json file
        panic(es.ERR_CMDFILE, 1)
    
    # make output dir
    make()
    
    # load configuration
    cfg = load()
    
    print(f'runbook execute:\n\tcommands={len(cfg)}')
    
    # main loop on commands
    for item in cfg:
        print(f'\nrunning:\n\tname={item["name"]}\n\tcommand={item["command"]}\n\tsyscall={item["syscall"]}')
        
        # check for systemcall type
        if bool(item["syscall"]):
            handle_syscall(item["command"], True)
            print(f'running syscall {item["name"]} is done.')
        else:
            location = handle_command(item)
            print(f'running {item["name"]} is done.\n\tlocation={location}')
    
    print("runbook executed.")


if __name__ == "__main__":
    main()
