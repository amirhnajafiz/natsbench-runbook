import sys
import logging


"""panic is used when you want to exit the application with an error.

params:
    - err: string
    - code: int
"""
def panic(err: str, code: int):
    logging.critical(err)
    sys.exit(code)
