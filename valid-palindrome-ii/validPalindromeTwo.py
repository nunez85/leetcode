def validPalindromeMySolution(s: str) -> bool:
    i, j = 0, len(s) - 1
    nextIToTry = -1
    nextJToTry = -1
    count = 0
    while i < j and i < len(s) and j > -1:
        
        if s[i] != s[j]:
            if count > 1:
                return False

            if nextIToTry != -1:
                i = nextIToTry
                j = nextJToTry
                count += 1
            elif i+1 < len(s) and s[i+1] == s[j]:
                nextIToTry = i
                nextJToTry = j - 1
                i += 1
                count += 1
            elif j-1 > -1 and s[i] == s[j-1]:
                nextIToTry = i + 1
                nextJToTry = j
                j -= 1
                count += 1
            else:
                return False
        else:
            i += 1
            j -= 1

    return True
  

class Solution:
  def validPalindrome(self, s: str) -> bool:
      i, j = 0, len(s) - 1
      
      while i < j:
          if s[i] == s[j]:
              i += 1
              j -= 1
          else:
              return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
      return True

  def validPalindromeUtil(self, s, i, j):
      while i < j:
          if s[i] == s[j]:
              i += 1
              j -= 1
          else:
              return False
      
      return True
