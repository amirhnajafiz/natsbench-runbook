# reader module is used to parse files
import os.path


CMDPATH = "cmd.json"

"""exists method checks for cmd.json file, and makes sure that
the CMDPATH file exists.

returns:
    - boolean
"""
def exists() -> bool:
    return os.path.isfile(CMDPATH)
