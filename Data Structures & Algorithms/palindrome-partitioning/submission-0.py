class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = list()
        curPartition = list()

        def dfs(i):
            if i >= len(s):
                palindromePartitions.append(curPartition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    curPartition.append(s[i:j + 1])
                    dfs(j + 1)
                    curPartition.pop()
        
        dfs(0)
        return palindromePartitions