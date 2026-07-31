class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        foundNums = {}

        for num in nums:
            if num in foundNums: continue
            foundNums[num] = True
        
        maxSeq = 0

        for num in foundNums:
            # If num - 1 exists, then it isn't the start of a sequence,
            # and it can be skipped without issue as an O(1) check.
            if num - 1 in foundNums: continue
            # Checking for the whole sequence as soon as a num - 1 isn't found
            # will capture any previous unique numbers that weren't the start of
            # the sequence.
            else:
                curSeq = 1
                seqNum = num

                while seqNum + 1 in foundNums:
                    curSeq += 1
                    seqNum += 1
                
                maxSeq = max(maxSeq, curSeq)
        
        return maxSeq
            

            


        
