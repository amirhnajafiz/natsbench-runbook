# todo: create a tmp directory
# todo: parse cmd.json file
# todo: create a dir for each command in tmp
# todo: execute each command base on its count
# todo: save the results into files (csv metrics and cmd output)
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
    
    for item in cfg:
        for index in range(0, int(item["count"])):
            # reserve the output dir
            id = writer.new_command()
            
            # execute the command
            out, err = run(item["command"], writer.get_location(id))
            if err: # check for errors
                logging.debug(out)
                logging.warning(es.ERR_EXEC_COMMAND)
            
            # export output
            writer.export(out.strip(), id, index)


if __name__ == "__main__":
    main()
