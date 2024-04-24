SUBKEY = "Sub stats"
PUBKEY = "Pub stats"
OVERALLKEY = "Pub/Sub stats"


"""raw parsing is used to export essential benchmark
data from the output of a benchmakr.

params:
    - text: string

returns:
    - string
"""
def raw_parsing(text: str) -> str:
    # split the whole text by enters
    parts = text.split("\n")
    
    pub, sub, over = "", "", ""
    
    for part in parts:
        token = part.strip()
        if OVERALLKEY in token:
            over = token
        elif PUBKEY in token:
            pub = token
        elif SUBKEY in token:
            sub = token
    
    return f'{pub}\n{sub}\n{over}\n'
