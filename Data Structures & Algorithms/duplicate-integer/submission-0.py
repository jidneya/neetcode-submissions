from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)
        for i in x.keys():
            if x[i] > 1:
                return True
        return False        

        