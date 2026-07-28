class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramSets = []

        while len(strs) != 0:
            curAnagram = strs[0]
            strs.remove(curAnagram)
            matchingAnagrams = [curAnagram]
            i = 0

            while i < len(strs):
                if sorted(curAnagram) == sorted(strs[i]):
                    matchingAnagrams.append(strs[i])
                    strs.remove(strs[i])
                else:
                    i += 1
            
            anagramSets.append(matchingAnagrams)
            
        return anagramSets