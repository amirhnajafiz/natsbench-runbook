import os
import uuid

from . import OUTPUTDIR


"""get destination location is a helper function that returns
the storing dir of a command.

params:
    - uid: string
    
returns:
    - string
"""
def __get_destination_location(uid: str) -> str:
    return f'{OUTPUTDIR}/{uid}'


"""new command creates a new directory for a command.

returns:
    - string
"""
def new_command(name: str) -> str:
    uid = f'{name}.{str(uuid.uuid4())[:2]}'
    
    dest = __get_destination_location(uid)
    os.mkdir(dest)
    
    return dest


"""load function gets a uid and returns the storage location.

params:
    - uid: string
    
returns:
    - string
"""
def load(uid: str) -> str:
    return __get_destination_location(uid)


"""export function is used to create an output file in
the given destination.

params:
    - context: string
    - locations: string
"""
def export(context: str, location: str):
    with open(location, 'w') as file:
        file.write(context)
