class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in sequences:
                current = num
                sequence = 1
                while current + 1 in sequences:
                    current += 1
                    sequence += 1
                longest = max (sequence, longest)
        return longest 
        