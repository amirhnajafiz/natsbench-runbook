"""check whether `name` is on PATH and marked as executable."""
def __is_tool(name):
    # from whichcraft import which
    from shutil import which

    return which(name) is not None


"""depcheck checks the installed tools before starting runbook.

returns:
    - bool
"""
def depcheck() -> bool:
    deplist = ["nats"]
    flag = True
    
    for dep in deplist:
        flag = flag and __is_tool(dep)
    
    return flag
