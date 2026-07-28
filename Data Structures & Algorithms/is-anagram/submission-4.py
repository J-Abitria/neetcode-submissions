class Solution:
    # Runs in O(n log n) time.
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings can't be anagrams if they're not the same length.
        if len(s) != len(t):
            return False

        # Create dictionaries for encountered letters.
        sDict = {}
        tDict = {}

        # Runs over entire length of array. O(n) time.
        for i in range(len(s)):
            # If the letter hasn't been countered yet, track it. Otherwise,
            # record another occurrence. (Both map searches are log(n) time)
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1

            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        
        # Check between each dictionary and see if the keys/values are equal.
        # Takes O(n) time.
        return sDict == tDict

