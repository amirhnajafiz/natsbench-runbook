# exporter is used to create output files
import os.path


OUTPUTDIR = "tmp"

"""make method checks for tmp dir, and makes sure that
the OUTPUTDIR exists.
"""
def make():
    if not os.path.isdir(OUTPUTDIR):
        os.mkdir(OUTPUTDIR)
