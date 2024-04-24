from .writer import export

import json


"""create metafile gets the command data in dictionary and creates a info.json
in the destination.

params:
    - context: dictionary
    - location: string
"""
def create_metafile(context: dict, location: str):
    data = json.dumps(context, indent=4, sort_keys=True, default=str)
    path = f'{location}/info.json'
    export(data, path)
