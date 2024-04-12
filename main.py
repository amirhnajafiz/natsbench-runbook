# todo: create a parser to read these csv's and calculate the average in each file + a dataset
# todo: perform Hypothesis test on the results for final output
from system.error import panic
from internal.config import exists
from internal.config.config import load
from internal.cmd.cmd import run, syscall
from internal.exporter import make
from internal.exporter.csv import export_dataset
import internal.exporter.writer as writer
from internal.exporter.gc import cleanup
from internal.parser.parser import raw_parsing
from internal.parser.dataset import create_dataset

import errors as es

import logging


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
        print(f'running:\n\tname={item["name"]}\n\tcommand={item["command"]}\n\tsyscall={item["syscall"]}')
        
        # check for systemcall type
        if bool(item["syscall"]):
            out, err = syscall(item["command"])
            logging.debug(out)
            if err: # check for errors
                logging.warning(es.ERR_EXEC_COMMAND)
            continue
        
        # reserve the output dir
        location = writer.new_command(item["name"])
        bound = int(item["count"])+1

        # loop on the count of each command
        for index in range(1, bound):            
            # execute the command
            raw, err = run(item["command"], f'{location}/xcmd-{index}.csv')
            if err: # check for errors
                logging.debug(raw)
                logging.warning(es.ERR_EXEC_COMMAND)
                cleanup(location)
                continue
            
            # parse the raw output
            out = raw_parsing(raw.strip())
            
            # export outputs
            writer.export(raw, f'{location}/xcmd-{index}.raw')
            writer.export(out, f'{location}/xcmd-{index}.out')
        
        # create the result dataset and save it
        ds = create_dataset(location)
        export_dataset(f'{location}/dataset.csv', ds)
        
        print(f'running {item["name"]} is done.\n\tlocation={location}')


if __name__ == "__main__":
    main()
