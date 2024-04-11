import json
from . import CMDPATH


"""load function reads cmd.json file into a dictionary.

returns:
    - dictionary
"""
def load() -> dict:
    with open(CMDPATH, "r") as file:
        return json.load(file)
