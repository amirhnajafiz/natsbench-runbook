# todo: create a tmp directory
# todo: parse cmd.json file
# todo: create a dir for each command in tmp
# todo: execute each command base on its count
# todo: save the results into files (csv metrics and cmd output)
# todo: create a parser to read these csv's and calculate the average in each file + a dataset
# todo: perform Hypothesis test on the results for final output
from system.error import panic
from internal.config import exists
from internal.config import load
from internal.cmd.cmd import run

import errors as es


def main():
    if not exists():
        panic(es.ERR_CMDFILE, 1)
    
    cfg = load()
    
    for item in cfg:
        for index in range(0, int(item["count"])):
            out = run(cfg["command"])
            print(index, out)


if __name__ == "__main__":
    main()
