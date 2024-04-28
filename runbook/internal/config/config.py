import json
from . import CMDPATH


"""load function reads cmd.json file into a dictionary.

params:
    - jsonContext: string

returns:
    - dictionary
"""
def load(jsonContext: str) -> dict:
    if len(jsonContext) > 0:
        return json.loads(jsonContext)
    
    with open(CMDPATH, "r") as file:
        return json.load(file)
