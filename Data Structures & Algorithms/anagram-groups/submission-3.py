class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Original approach, too slow!

        # Time complexity: O(n^2 * m log m)
        # A list for the strings determined to be anagrams of one another.
        anagramSets = []

        # Runs until all strings have been categorized. O(n) worst case.
        while len(strs) != 0:
            # Grab the next unmatched string in the list.
            curAnagram = strs[0]
            # Remove the string from that list to prevent duplicates.
            strs.remove(curAnagram)
            # Make a new list of the set of strings that are anagrams.
            matchingAnagrams = [curAnagram]
            i = 0

            while i < len(strs):
                # For each string in the list, if they have the same characters,
                # add it to the list of matchingAnagrams, and remove it from the
                # unmatched strings list. Don't increment due to list changing.
                # O(m log m) for each sort, O(n) for while loop.
                if sorted(curAnagram) == sorted(strs[i]):
                    matchingAnagrams.append(strs[i])
                    strs.remove(strs[i])
                # Otherwise, skip that string.
                else:
                    i += 1
            
            # After all anagrams are found, append that set to the list of all sets.
            anagramSets.append(matchingAnagrams)
        """
        # A list for the list of anagrams, and the unique sets of characters.
        anagramSets = []
        encounteredCharSets = {}
        uniqueSets = 0

        # Iterates over the list in O(n) time.
        while len(strs) != 0:
            # Sorts each string in O(m log m) time.
            charSet = str(sorted(strs[0]))

            # If the character set was not found in the map, insert it and update the number
            # of unique anagrams.
            if charSet not in encounteredCharSets:
                encounteredCharSets[charSet] = uniqueSets
                anagramSets.append([strs[0]])
                uniqueSets += 1
            # Otherwise, from the index tracked in the map, add that string to the mapped anagram
            # index.
            else:
                anagramSets[encounteredCharSets[charSet]].append(strs[0])
            
            # Always remove a string that has been categorized.
            strs.remove(strs[0])
            
        return anagramSets