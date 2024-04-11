# exporter is used to create output files
import os.path


OUTPUTDIR = "tmp"

"""exists method checks for tmp dir, and makes sure that
the OUTPUTDIR exists.
"""
def exists() -> bool:
    return os.path.isdir(OUTPUTDIR)
