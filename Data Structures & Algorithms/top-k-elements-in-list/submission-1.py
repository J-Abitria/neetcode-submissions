class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num, occurrences in count.items():
            freq[occurrences].append(num)
        
        mostFreqElements = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                mostFreqElements.append(num)
            
                if len(mostFreqElements) == k:
                    return mostFreqElements
        
