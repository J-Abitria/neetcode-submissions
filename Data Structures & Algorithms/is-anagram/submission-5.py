class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreqTableS = {}
        charFreqTableT = {}

        for char in s:
            if char not in charFreqTableS:
                charFreqTableS[char] = 1
            
            charFreqTableS[char] += 1
        
        for char in t:
            if char not in charFreqTableT:
                charFreqTableT[char] = 1
            
            charFreqTableT[char] += 1
        
        return charFreqTableS == charFreqTableT