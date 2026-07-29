class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for word in strs:
            freqTable = [0] * 26

            for letter in word:
                freqTable[ord(letter) - ord('a')] += 1
            
            key = "#".join([str(num) for num in freqTable])

            if key in wordDict:
                wordDict[key].append(word)
            else:
                wordDict[key] = [word]
        

        answer = []

        for key in wordDict:
            answer.append(wordDict[key])
        
        return answer