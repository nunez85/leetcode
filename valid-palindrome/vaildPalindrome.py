def isPalindrome(s: str) -> bool:
    lowercased_alpha = "".join([st.lower() for st in s if st.isalnum()])
    if len(lowercased_alpha) <= 1:
        return True
    left = 0
    right = len(lowercased_alpha) - 1

    while left <= right:
        if lowercased_alpha[left] != lowercased_alpha[right]:
            return False
        left += 1
        right -= 1

    return True