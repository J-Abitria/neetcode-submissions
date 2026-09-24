class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        possibleStrings = list()
        def dfs(i, curString):
            if len(curString) == len(digits):
                possibleStrings.append(curString)
                return
            
            for letter in digitMapping[digits[i]]:
                curString += letter
                dfs(i + 1, curString)
                curString = curString[:-1]
        
        if len(digits) > 0:
            dfs(0, "")
        
        return possibleStrings