class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterFreq = {}
        maxFreq = 0
        maxSequence = 0
        start = end = 0

        while end < len(s):
            if s[end] not in letterFreq: letterFreq[s[end]] = 1
            else: letterFreq[s[end]] += 1
            maxFreq = max(maxFreq, letterFreq[s[end]])

            end += 1
            if len(s[start:end]) - maxFreq > k:
                letterFreq[s[start]] -= 1
                start += 1
            else:
                maxSequence = max(maxSequence, len(s[start:end]))
            
        return maxSequence