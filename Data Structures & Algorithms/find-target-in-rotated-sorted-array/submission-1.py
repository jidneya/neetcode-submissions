class Solution:
    def search(self, nums: List[int], target: int) -> int:
        split = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                split = i
                break
            

        l, r = 0, split
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        l, r = split+1, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1
        
        