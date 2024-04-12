import os


"""cleanup methos is used to clean empty directorys.

params:
    - location: string
"""
def cleanup(location: str):
    os.rmdir(location)
