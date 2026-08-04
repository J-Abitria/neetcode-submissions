class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # Using the index conditions to allow for an easier to read if condition.
        while left < len(s) and right > 0 and left < right:
            """
            If before checking equality, the left or right side pointer has
            a non-alphanumeric character, it moves the pointer and restarts
            the loop entirely.
            """
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower(): return False

            left += 1
            right -= 1
        
        return True