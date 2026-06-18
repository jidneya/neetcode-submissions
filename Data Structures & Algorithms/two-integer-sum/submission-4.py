class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            aim = target - nums[i]
            if aim in nums:
                try:
                    return [i, nums.index(aim, i+1, len(nums))]
                except:
                    pass

        