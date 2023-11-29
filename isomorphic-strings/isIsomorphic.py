def normalizeString(s: str) -> List[int]:
    nmap = {}
    i = 0
    normalized = []

    for char in s:
        if char not in nmap:
            nmap[char] = i
            i += 1
        
        normalized.append(nmap[char])

    return normalized

def isIsomorphic(self, s: str, t: str) -> bool:
    return normalizeString(s) == normalizeString(t)

