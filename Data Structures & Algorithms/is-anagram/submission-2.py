class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1

            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        
        return sDict == tDict

