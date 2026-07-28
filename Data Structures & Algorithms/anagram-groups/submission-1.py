class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A list for the strings determined to be anagrams of one another.
        anagramSets = []

        # Runs until all strings have been categorized.
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
                if sorted(curAnagram) == sorted(strs[i]):
                    matchingAnagrams.append(strs[i])
                    strs.remove(strs[i])
                # Otherwise, skip that string.
                else:
                    i += 1
            
            # After all anagrams are found, append that set to the list of all sets.
            anagramSets.append(matchingAnagrams)
            
        return anagramSets