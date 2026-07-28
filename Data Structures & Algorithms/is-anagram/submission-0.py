class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        encounteredCharsS = {}
        encounteredCharsT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in encounteredCharsS:
                encounteredCharsS[s[i]] = 1
            else:
                encounteredCharsS[s[i]] += 1
            
            if t[i] not in encounteredCharsT:
                encounteredCharsT[t[i]] = 1
            else:
                encounteredCharsT[t[i]] += 1
        
        if encounteredCharsS == encounteredCharsT:
            return True
        return False
        