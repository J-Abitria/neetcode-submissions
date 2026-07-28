class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freqTable = [0] * 26

        for i in range(len(s)):
            freqTable[ord(s[i]) - ord('a')] += 1
            freqTable[ord(t[i]) - ord('a')] -= 1

        for letter in freqTable:
            if letter != 0: return False
        
        return True