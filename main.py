# todo: create a parser to read these csv's and calculate the average in each file + a dataset
# todo: perform Hypothesis test on the results for final output
from system.error import panic
from internal.config import exists
from internal.config.config import load
from internal.cmd.cmd import run
from internal.exporter import make
import internal.exporter.writer as writer

import errors as es

import logging


def main():
    if not exists(): # check the cmd.json file
        panic(es.ERR_CMDFILE, 1)
    
    # make output dir
    make()
    
    # load configuration
    cfg = load()
    
    # main loop on commands
    for item in cfg:
        # reserve the output dir
        location = writer.new_command()

        for index in range(0, int(item["count"])):            
            # execute the command
            out, err = run(item["command"], f'{location}/{index}.out.csv')
            if err: # check for errors
                logging.debug(out)
                logging.warning(es.ERR_EXEC_COMMAND)
                continue
            
            # export output
            writer.export(out.strip(), f'{location}/{index}.out')


if __name__ == "__main__":
    main()
