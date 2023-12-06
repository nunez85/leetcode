class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    left = 0
    maximum = 0

    for right in range(len(s)):
      while s[right] in charSet:
        charSet.remove(s[left])
        left += 1
        
      charSet.add(s[right])
      maximum = max(maximum, right - left + 1)
    return maximum


  def secondTry(self, s: str) -> int:
    if len(s) < 1:
      return 0

    maximum = float('-inf')
    subset = set()
    i = 0

    while i < len(s):
      if s[i] in subset:
        subset.clear()
        subset.add(s[i])
        j = i - 1
        while j > 0 and s[i] != s[j]:
          subset.add(s[j])
          j -= 1
        
        
      else:
        subset.add(s[i])
        maximum = max(maximum, len(subset))

      i += 1

    return int(maximum)
    

  def firstTry(self, s: str) -> int:
    if len(s) < 1:
      return 0

    unique = set()
    max_length = float('-inf')
    current_sub = ""
    i = 0
    while i < len(s):
      if len(current_sub) > 0:
        if s[i] not in current_sub:
          current_sub += s[i] 
          max_length = max(max_length, len(current_sub))
        else:
          current_sub = s[i]
          j = i - 1
          while j > 0 and s[j] != s[i]:
            current_sub = s[j] + current_sub
            j -= 1
          max_length = max(max_length, len(current_sub))
      else:
        current_sub = s[i]
        max_length = 1
      i += 1

    return int(max_length)
