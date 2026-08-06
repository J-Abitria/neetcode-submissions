class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        foundChars = {}
        start = 0
        maxSeq = curSeq = 0

        for end in range(len(s)):
            if s[end] in foundChars:
                maxSeq = max(maxSeq, curSeq)

                while start != end and s[end] in foundChars:
                    del foundChars[s[start]]
                    curSeq -= 1
                    start += 1
            
            foundChars[s[end]] = True
            curSeq += 1
        
        return max(maxSeq, curSeq)