class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        freqTable = [0] * 26

        for i in range(len(s1)):
            freqTable[ord(s1[i]) - ord('a')] += 1
            freqTable[ord(s2[i]) - ord('a')] -= 1
        
        matchedLetters = 0
        for i in range(len(freqTable)):
            if freqTable[i] == 0: matchedLetters += 1

        start, end = 0, len(s1) - 1
        while end < len(s2):
            if matchedLetters == 26: return True

            startLetterIdx = ord(s2[start]) - ord('a')
            freqTable[startLetterIdx] += 1
            if freqTable[startLetterIdx] == 1:
                matchedLetters -= 1
            elif freqTable[startLetterIdx] == 0:
                matchedLetters += 1
            
            start += 1
            end += 1

            if end == len(s2): break
            endLetterIdx = ord(s2[end]) - ord('a')
            freqTable[endLetterIdx] -= 1
            if freqTable[endLetterIdx] == -1:
                matchedLetters -= 1
            elif freqTable[endLetterIdx] == 0:
                matchedLetters += 1
        
        return matchedLetters == 26