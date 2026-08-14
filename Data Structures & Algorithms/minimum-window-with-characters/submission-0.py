class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        minSubstring = ""
        charFreq = {}
        neededMatches = 0
        for letter in t:
            if letter not in charFreq:
                charFreq[letter] = 1
                neededMatches += 1
            else:
                charFreq[letter] += 1
        
        windowFreq = {}
        start = end = 0
        while end < len(s):
            if s[end] not in windowFreq: windowFreq[s[end]] = 1
            else: windowFreq[s[end]] += 1

            if s[end] in charFreq and windowFreq[s[end]] == charFreq[s[end]]:
                neededMatches -= 1
            
            while neededMatches == 0:
                if minSubstring == "" or len(minSubstring) > (end - start + 1):
                    minSubstring = s[start:end + 1]
                
                windowFreq[s[start]] -= 1
                if s[start] in charFreq and windowFreq[s[start]] < charFreq[s[start]]:
                    neededMatches += 1
                start += 1

            end += 1
        
        return minSubstring

