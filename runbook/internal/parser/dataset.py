import os


SPLITOR = "~"
KBFLAG = "KB/sec"


"""import numbers is used to parse raw text line to a float number.

params:
    - context: string
    
returns:
    - float
"""
def __import_numbers(context: str) -> float:
    sections = context.split(SPLITOR)
    parts = sections[1].strip().split(" ")
    number = float(parts[0])
    
    if KBFLAG in parts[1]:
        number = float(number / 1000)
    
    return number


"""create dataset is used to parse .out files
into a 2d array.

params:
    - location: string
    
returns:
    - list
"""
def create_dataset(location: str) -> list:
    dataset = []
    
    files = [x for x in os.listdir(location) if x.endswith(".out")]
    for filename in files:
        with open(f'{location}/{filename}', "r") as f:
            lines = f.readlines()
            array = []
            for line in lines:
                if len(line) > 2:
                    array.append(__import_numbers(line.strip()))
            dataset.append(array)
    
    return dataset
