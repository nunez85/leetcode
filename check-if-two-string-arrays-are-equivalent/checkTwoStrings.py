def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    pt1, pt2 = 0, 0
    idx1, idx2 = 0, 0
    while pt1 < len(word1) and pt2 < len(word2):
        if word1[pt1][idx1] != word2[pt2][idx2]:
            return False

        if idx1 + 1 == len(word1[pt1]):
            idx1 = 0
            pt1 += 1
        else:
            idx1 += 1


        if idx2 + 1 == len(word2[pt2]):
            idx2 = 0
            pt2 += 1
        else:
            idx2 += 1

        
    return pt1 == len(word1) and pt2 == len(word2)
