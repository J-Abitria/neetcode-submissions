class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        This is the best solution with tricks, but it can also be done with
        a max heap! REDO THIS PROBLEM WITH HEAP
        """
        # Create a map to count number of occurrences, and an
        # array for bucket sort, where the index represents the number
        # of occurrences that a number has in nums, and the value is a list
        # of what numeric values occur that many times.
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Iterates through the list, counts how many times each number
        # occurs in the list and tracks it in the map.
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # Access a specific list by index through the number of occurrences as
        # the value for this numeric value, and append to it the number stored as
        # the key in the map.
        for num, occurrences in count.items():
            freq[occurrences].append(num)
        
        mostFreqElements = []

        # Starting from the end of the frequency array, append items to the most
        # frequent elements list until the length matches the value of k. Order
        # Doesn't matter as the problem states they can be returned in any order.
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                mostFreqElements.append(num)
            
                if len(mostFreqElements) == k:
                    return mostFreqElements
        
