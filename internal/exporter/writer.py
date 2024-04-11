import os
import uuid

from . import OUTPUTDIR


def get_location(uid: str) -> str:
    return f'{OUTPUTDIR}/{uid}'

def new_command() -> str:
    uid = str(uuid.uuid4())
    os.mkdir(f'{OUTPUTDIR}/{uid}')
    
    return uid

def export(context: str, uid: str, index: int):
    with open(f'{get_location(uid)}/out.{index}', 'w') as file:
        file.write(context)
