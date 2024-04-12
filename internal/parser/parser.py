SUBKEY = "Sub stats"
PUBKEY = "Pub stats"
OVERALLKEY = "Pub/Sub stats"


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
