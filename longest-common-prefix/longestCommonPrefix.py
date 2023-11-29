
def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    max_length = len(min(strs, key=len))
    word = strs[0]
    prefix = ""

    for i in range(max_length):
        for s in strs:
            if word[i] != s[i]:
                return prefix
        
        prefix += word[i]

    return prefix

