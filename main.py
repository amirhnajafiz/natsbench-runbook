# todo: create a parser to read these csv's and calculate the average in each file + a dataset
# todo: perform Hypothesis test on the results for final output
from system.error import panic
from internal.config import exists
from internal.config.config import load
from internal.cmd.cmd import run, syscall
from internal.exporter import make
import internal.exporter.writer as writer
from internal.exporter.gc import cleanup
from internal.parser.parser import raw_parsing

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
    
    # main loop on commands
    for item in cfg:
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

        for index in range(1, bound):            
            # execute the command
            raw, err = run(item["command"], f'{location}/cmd-{index}.csv')
            if err: # check for errors
                logging.debug(raw)
                logging.warning(es.ERR_EXEC_COMMAND)
                cleanup(location)
                continue
            
            # parse the raw output
            out = raw_parsing(raw.strip())
            
            # export outputs
            writer.export(raw, f'{location}/cmd-{index}.raw')
            writer.export(out, f'{location}/cmd-{index}.out')


if __name__ == "__main__":
    main()
